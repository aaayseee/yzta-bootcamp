"""Central database and authentication repository for LoyalCart.

SQLite is the default development database. MySQL can be selected with
``DB_ENGINE=mysql`` and the MYSQL_* environment variables.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import secrets
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from typing import Any, Dict, Iterable, List, Optional


PBKDF2_ITERATIONS = 390_000


class DuplicateUserError(ValueError):
    """Raised when a username or email address already exists."""


def _engine() -> str:
    return os.getenv("DB_ENGINE", "sqlite").strip().lower()


def _sqlite_path() -> str:
    return os.getenv("SQLITE_PATH", "loyalcart.db")


def _mysql_connector():
    try:
        import mysql.connector
    except ImportError as exc:
        raise RuntimeError(
            "DB_ENGINE=mysql için mysql-connector-python kurulmalıdır."
        ) from exc
    return mysql.connector


@contextmanager
def _connection():
    if _engine() == "mysql":
        connector = _mysql_connector()
        conn = connector.connect(
            host=os.getenv("MYSQL_HOST", "127.0.0.1"),
            port=int(os.getenv("MYSQL_PORT", "3306")),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD", ""),
            database=os.getenv("MYSQL_DB", "loyalcart"),
        )
    else:
        conn = sqlite3.connect(_sqlite_path())
        conn.row_factory = sqlite3.Row

    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def _placeholder() -> str:
    return "%s" if _engine() == "mysql" else "?"


def hash_password(password: str) -> str:
    if len(password) < 8:
        raise ValueError("Şifre en az 8 karakter olmalıdır.")
    salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, PBKDF2_ITERATIONS
    )
    return "pbkdf2_sha256${}${}${}".format(
        PBKDF2_ITERATIONS,
        base64.b64encode(salt).decode("ascii"),
        base64.b64encode(digest).decode("ascii"),
    )


def verify_password(password: str, encoded: str) -> bool:
    try:
        algorithm, iterations, salt_b64, digest_b64 = encoded.split("$", 3)
        if algorithm != "pbkdf2_sha256":
            return False
        salt = base64.b64decode(salt_b64)
        expected = base64.b64decode(digest_b64)
        actual = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), salt, int(iterations)
        )
        return hmac.compare_digest(actual, expected)
    except (TypeError, ValueError):
        return False


def _sqlite_columns(conn: sqlite3.Connection, table: str) -> set[str]:
    return {row[1] for row in conn.execute(f"PRAGMA table_info({table})").fetchall()}


def _ensure_sqlite_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            email TEXT NOT NULL,
            password_hash TEXT,
            role TEXT NOT NULL DEFAULT 'manager',
            is_active INTEGER NOT NULL DEFAULT 1,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );

        CREATE UNIQUE INDEX IF NOT EXISTS idx_users_email
        ON users(email COLLATE NOCASE);

        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id TEXT,
            features TEXT NOT NULL,
            prediction INTEGER NOT NULL,
            probability REAL,
            model_version TEXT,
            result TEXT,
            action TEXT,
            source TEXT NOT NULL DEFAULT 'api',
            created_by TEXT,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS audit_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            event_type TEXT NOT NULL,
            status TEXT NOT NULL,
            details TEXT,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        """
    )

    user_columns = _sqlite_columns(conn, "users")
    additions = {
        "password_hash": "TEXT",
        "is_active": "INTEGER NOT NULL DEFAULT 1",
        "created_at": "TEXT",
    }
    for column, definition in additions.items():
        if column not in user_columns:
            conn.execute(f"ALTER TABLE users ADD COLUMN {column} {definition}")

    prediction_columns = _sqlite_columns(conn, "predictions")
    prediction_additions = {
        "result": "TEXT",
        "action": "TEXT",
        "source": "TEXT NOT NULL DEFAULT 'api'",
        "created_by": "TEXT",
    }
    for column, definition in prediction_additions.items():
        if column not in prediction_columns:
            conn.execute(f"ALTER TABLE predictions ADD COLUMN {column} {definition}")

    # Transparently migrate legacy plaintext passwords, then remove their value.
    user_columns = _sqlite_columns(conn, "users")
    if "password" in user_columns:
        rows = conn.execute(
            "SELECT username, password FROM users "
            "WHERE password IS NOT NULL AND password != '' "
            "AND (password_hash IS NULL OR password_hash = '')"
        ).fetchall()
        for row in rows:
            password = row["password"]
            if len(password) >= 8:
                encoded = hash_password(password)
                conn.execute(
                    "UPDATE users SET password_hash = ?, password = '' WHERE username = ?",
                    (encoded, row["username"]),
                )


def _ensure_mysql_schema(conn) -> None:
    statements = [
        """
        CREATE TABLE IF NOT EXISTS users (
            username VARCHAR(128) PRIMARY KEY,
            email VARCHAR(255) NOT NULL UNIQUE,
            password_hash VARCHAR(512) NOT NULL,
            role VARCHAR(32) NOT NULL DEFAULT 'manager',
            is_active BOOLEAN NOT NULL DEFAULT TRUE,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """,
        """
        CREATE TABLE IF NOT EXISTS predictions (
            id BIGINT AUTO_INCREMENT PRIMARY KEY,
            customer_id VARCHAR(128),
            features JSON NOT NULL,
            prediction TINYINT NOT NULL,
            probability FLOAT,
            model_version VARCHAR(64),
            result VARCHAR(255),
            action TEXT,
            source VARCHAR(32) NOT NULL DEFAULT 'api',
            created_by VARCHAR(128),
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """,
        """
        CREATE TABLE IF NOT EXISTS audit_logs (
            id BIGINT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(128),
            event_type VARCHAR(64) NOT NULL,
            status VARCHAR(32) NOT NULL,
            details TEXT,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """,
    ]
    cursor = conn.cursor()
    try:
        for statement in statements:
            cursor.execute(statement)
    finally:
        cursor.close()


def initialize_database() -> None:
    with _connection() as conn:
        if _engine() == "mysql":
            _ensure_mysql_schema(conn)
        else:
            _ensure_sqlite_schema(conn)
    ensure_admin_from_environment()


def ensure_admin_from_environment() -> bool:
    password = os.getenv("LOYALCART_ADMIN_PASSWORD")
    if not password:
        return False
    username = os.getenv("LOYALCART_ADMIN_USERNAME", "admin").strip()
    email = os.getenv("LOYALCART_ADMIN_EMAIL", "admin@loyalcart.local").strip()
    existing = get_user(username)
    if existing:
        return True
    create_user(username, email, password, role="administrator")
    return True


def create_user(
    username: str, email: str, password: str, role: str = "manager"
) -> Dict[str, Any]:
    username = username.strip()
    email = email.strip().lower()
    if len(username) < 3:
        raise ValueError("Kullanıcı adı en az 3 karakter olmalıdır.")
    if "@" not in email:
        raise ValueError("Geçerli bir e-posta adresi girilmelidir.")
    if role not in {"administrator", "manager", "viewer"}:
        raise ValueError("Geçersiz kullanıcı rolü.")
    encoded = hash_password(password)
    p = _placeholder()
    sql = (
        "INSERT INTO users (username, email, password_hash, role, is_active) "
        f"VALUES ({p}, {p}, {p}, {p}, {p})"
    )
    try:
        with _connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (username, email, encoded, role, 1))
            cursor.close()
    except Exception as exc:
        message = str(exc).lower()
        if "unique" in message or "duplicate" in message or "integrity" in message:
            raise DuplicateUserError(
                "Kullanıcı adı veya e-posta adresi zaten kayıtlı."
            ) from exc
        raise
    return {"username": username, "email": email, "role": role}


def get_user(identifier: str) -> Optional[Dict[str, Any]]:
    p = _placeholder()
    sql = (
        "SELECT username, email, password_hash, role, is_active FROM users "
        f"WHERE LOWER(username) = LOWER({p}) OR LOWER(email) = LOWER({p})"
    )
    with _connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (identifier.strip(), identifier.strip()))
        row = cursor.fetchone()
        columns = [item[0] for item in cursor.description] if cursor.description else []
        cursor.close()
    if row is None:
        return None
    return dict(row) if isinstance(row, sqlite3.Row) else dict(zip(columns, row))


def authenticate_user(identifier: str, password: str) -> Optional[Dict[str, Any]]:
    user = get_user(identifier)
    if not user or not bool(user["is_active"]):
        return None
    if not verify_password(password, user["password_hash"] or ""):
        return None
    return {
        "username": user["username"],
        "email": user["email"],
        "role": user["role"],
    }


def record_audit(
    event_type: str,
    status: str,
    username: Optional[str] = None,
    details: Optional[str] = None,
) -> None:
    p = _placeholder()
    sql = (
        "INSERT INTO audit_logs (username, event_type, status, details) "
        f"VALUES ({p}, {p}, {p}, {p})"
    )
    with _connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (username, event_type, status, details))
        cursor.close()


def save_prediction(
    customer_id: Optional[str],
    features: Dict[str, Any],
    prediction: int,
    probability: float,
    model_version: Optional[str] = None,
    result: Optional[str] = None,
    action: Optional[str] = None,
    source: str = "api",
    created_by: Optional[str] = None,
) -> int:
    p = _placeholder()
    sql = (
        "INSERT INTO predictions "
        "(customer_id, features, prediction, probability, model_version, "
        "result, action, source, created_by) "
        f"VALUES ({', '.join([p] * 9)})"
    )
    values = (
        customer_id,
        json.dumps(features, ensure_ascii=False, default=str),
        int(prediction),
        float(probability),
        model_version,
        result,
        action,
        source,
        created_by,
    )
    with _connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, values)
        prediction_id = int(cursor.lastrowid)
        cursor.close()
    return prediction_id


def list_predictions(limit: int = 1000) -> List[Dict[str, Any]]:
    limit = max(1, min(int(limit), 5000))
    p = _placeholder()
    sql = (
        "SELECT id, created_at, customer_id, result, probability, prediction, "
        "action, source, created_by, model_version, features "
        f"FROM predictions ORDER BY created_at DESC, id DESC LIMIT {p}"
    )
    with _connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (limit,))
        rows = cursor.fetchall()
        columns = [item[0] for item in cursor.description] if cursor.description else []
        cursor.close()
    if _engine() == "mysql":
        return [dict(zip(columns, row)) for row in rows]
    return [dict(row) for row in rows]


def clear_predictions() -> None:
    with _connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM predictions")
        cursor.close()

