-- MySQL initialization script for LoyalCart app
CREATE DATABASE IF NOT EXISTS loyalcart CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE loyalcart;

CREATE TABLE IF NOT EXISTS predictions (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  customer_id VARCHAR(128) DEFAULT NULL,
  features JSON DEFAULT NULL,
  prediction TINYINT NOT NULL,
  probability FLOAT DEFAULT NULL,
  model_version VARCHAR(64) DEFAULT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- You can add more tables (users, audits) below as needed
