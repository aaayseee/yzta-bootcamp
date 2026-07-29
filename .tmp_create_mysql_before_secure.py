"""Helper script to create MySQL database and `predictions` table.

Usage:
  - Install driver: pip install mysql-connector-python
  - Set environment variables: MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
  - Run: python scripts/create_mysql_db.py
"""
import os
import sys

try:
    import mysql.connector
    from mysql.connector import errorcode
except Exception as e:
    print("Missing dependency: mysql-connector-python. Install with: pip install mysql-connector-python")
    raise

HOST = os.getenv('MYSQL_HOST', '127.0.0.1')
PORT = int(os.getenv('MYSQL_PORT', '3306'))
USER = os.getenv('MYSQL_USER', 'root')
PASSWORD = os.getenv('MYSQL_PASSWORD', '')
DB_NAME = os.getenv('MYSQL_DB', 'loyalcart')

SQL_CREATE_DB = f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
SQL_USE_DB = f"USE `{DB_NAME}`;"
SQL_CREATE_TABLE = '''
CREATE TABLE IF NOT EXISTS predictions (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  customer_id VARCHAR(128) DEFAULT NULL,
  features JSON DEFAULT NULL,
  prediction TINYINT NOT NULL,
  probability FLOAT DEFAULT NULL,
  model_version VARCHAR(64) DEFAULT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
'''


def main():
    try:
        conn = mysql.connector.connect(host=HOST, port=PORT, user=USER, password=PASSWORD)
        conn.autocommit = True
        cursor = conn.cursor()
        print(f"Connected to MySQL at {HOST}:{PORT} as {USER}")

        print(f"Creating database `{DB_NAME}` if not exists...")
        cursor.execute(SQL_CREATE_DB)
        print("Database ensured.")

        # Use DB and create table
        cursor.execute(SQL_USE_DB)
        print("Creating `predictions` table if not exists...")
        cursor.execute(SQL_CREATE_TABLE)
        print("Table `predictions` ensured.")

        cursor.close()
        conn.close()
        print("Done.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied: check MYSQL_USER and MYSQL_PASSWORD")
        else:
            print(f"MySQL error: {err}")
        sys.exit(1)


if __name__ == '__main__':
    main()
