CREATE DATABASE IF NOT EXISTS loyalcart
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE loyalcart;

CREATE TABLE IF NOT EXISTS users (
  username VARCHAR(128) PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(512) NOT NULL,
  role VARCHAR(32) NOT NULL DEFAULT 'manager',
  is_active BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_predictions_created_at (created_at),
  INDEX idx_predictions_customer_id (customer_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS audit_logs (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(128),
  event_type VARCHAR(64) NOT NULL,
  status VARCHAR(32) NOT NULL,
  details TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_audit_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
