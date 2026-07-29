"""Create the LoyalCart MySQL database and application tables."""

import os
import sys

try:
    import mysql.connector
except ImportError:
    print("mysql-connector-python kurulmalıdır.")
    raise


def main():
    host = os.getenv("MYSQL_HOST", "127.0.0.1")
    port = int(os.getenv("MYSQL_PORT", "3306"))
    user = os.getenv("MYSQL_USER", "root")
    password = os.getenv("MYSQL_PASSWORD", "")
    database = os.getenv("MYSQL_DB", "loyalcart")

    try:
        connection = mysql.connector.connect(
            host=host, port=port, user=user, password=password
        )
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS `{database}` "
            "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
        )
        cursor.close()
        connection.close()

        os.environ["DB_ENGINE"] = "mysql"
        from db.repository import initialize_database

        initialize_database()
        print(f"`{database}` veritabanı ve LoyalCart tabloları hazır.")
    except mysql.connector.Error as exc:
        print(f"MySQL hatası: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
