"""Password reset and integration event persistence."""

import hashlib
import secrets
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional, Tuple

import sqlite3

from db.repository import (
    _connection,
    _engine,
    _placeholder,
    get_user,
    hash_password,
)


def initialize_security_tables() -> None:
    with _connection() as conn:
        cursor = conn.cursor()
        if _engine() == "mysql":
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS password_reset_tokens (
                    id BIGINT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(128) NOT NULL,
                    token_hash CHAR(64) NOT NULL UNIQUE,
                    expires_at DATETIME NOT NULL,
                    used_at DATETIME,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
                """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS integration_events (
                    id BIGINT AUTO_INCREMENT PRIMARY KEY,
                    provider VARCHAR(32) NOT NULL,
                    event_type VARCHAR(64) NOT NULL,
                    status VARCHAR(32) NOT NULL,
                    message TEXT,
                    created_by VARCHAR(128),
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
                """
            )
        else:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS password_reset_tokens (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    token_hash TEXT NOT NULL UNIQUE,
                    expires_at TEXT NOT NULL,
                    used_at TEXT,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS integration_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    provider TEXT NOT NULL,
                    event_type TEXT NOT NULL,
                    status TEXT NOT NULL,
                    message TEXT,
                    created_by TEXT,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
        cursor.close()


def create_password_reset_token(
    identifier: str, ttl_minutes: int = 30
) -> Optional[Tuple[str, str]]:
    user = get_user(identifier)
    if not user or not bool(user["is_active"]):
        return None

    raw_token = secrets.token_urlsafe(32)
    token_hash = hashlib.sha256(raw_token.encode("utf-8")).hexdigest()
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=ttl_minutes)
    p = _placeholder()
    with _connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"DELETE FROM password_reset_tokens WHERE username = {p} AND used_at IS NULL",
            (user["username"],),
        )
        cursor.execute(
            "INSERT INTO password_reset_tokens "
            "(username, token_hash, expires_at) "
            f"VALUES ({p}, {p}, {p})",
            (user["username"], token_hash, expires_at.replace(tzinfo=None)),
        )
        cursor.close()
    return raw_token, user["email"]


def reset_password(token: str, new_password: str) -> bool:
    token_hash = hashlib.sha256(token.encode("utf-8")).hexdigest()
    p = _placeholder()
    with _connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, username, expires_at, used_at FROM password_reset_tokens "
            f"WHERE token_hash = {p}",
            (token_hash,),
        )
        row = cursor.fetchone()
        columns = [item[0] for item in cursor.description] if cursor.description else []
        if row is None:
            cursor.close()
            return False
        item = dict(row) if isinstance(row, sqlite3.Row) else dict(zip(columns, row))
        expires_at = item["expires_at"]
        if isinstance(expires_at, str):
            expires_at = datetime.fromisoformat(expires_at)
        if expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=timezone.utc)
        if item["used_at"] is not None or expires_at <= datetime.now(timezone.utc):
            cursor.close()
            return False

        encoded = hash_password(new_password)
        cursor.execute(
            f"UPDATE users SET password_hash = {p} WHERE username = {p}",
            (encoded, item["username"]),
        )
        cursor.execute(
            f"UPDATE password_reset_tokens SET used_at = {p} WHERE id = {p}",
            (datetime.now(timezone.utc).replace(tzinfo=None), item["id"]),
        )
        cursor.close()
    return True


def record_integration_event(
    provider: str,
    event_type: str,
    status: str,
    message: str,
    created_by: Optional[str] = None,
) -> int:
    p = _placeholder()
    with _connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO integration_events "
            "(provider, event_type, status, message, created_by) "
            f"VALUES ({', '.join([p] * 5)})",
            (provider, event_type, status, message, created_by),
        )
        event_id = int(cursor.lastrowid)
        cursor.close()
    return event_id


def list_integration_events(limit: int = 200) -> List[Dict[str, Any]]:
    limit = max(1, min(int(limit), 1000))
    p = _placeholder()
    with _connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, provider, event_type, status, message, created_by, created_at "
            f"FROM integration_events ORDER BY created_at DESC, id DESC LIMIT {p}",
            (limit,),
        )
        rows = cursor.fetchall()
        columns = [item[0] for item in cursor.description] if cursor.description else []
        cursor.close()
    if _engine() == "mysql":
        return [dict(zip(columns, row)) for row in rows]
    return [dict(row) for row in rows]


def clear_integration_events() -> None:
    with _connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM integration_events")
        cursor.close()

