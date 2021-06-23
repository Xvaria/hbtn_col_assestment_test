-- Create database and user to project
-- If database or user exist don't fail
CREATE DATABASE IF NOT EXISTS hbtn_col;
CREATE USER IF NOT EXISTS 'admin_01'@'localhost' IDENTIFIED BY 'admin_01_pwd';
GRANT ALL PRIVILEGES ON hbtn_col . * TO 'admin_01'@'localhost';
FLUSH PRIVILEGES;
USE hbtn_col;
CREATE TABLE IF NOT EXISTS users (
	   name VARCHAR(256),
	   lastname VARCHAR(256),
	   gov_id INT,
	   email VARCHAR(256),
	   company VARCHAR(256)
)
CREATE TABLE IF NOT EXISTS order (
	   date VARCHAR(256),
	   total VARCHAR(256),
	   subtotal INT,
	   taxes VARCHAR(256),
	   paid VARCHAR(256)
)
CREATE TABLE IF NOT EXISTS shipping (
	   address VARCHAR(256),
	   city VARCHAR(256),
	   state VARCHAR(256),
	   country VARCHAR(256),
	   cost VARCHAR(256)
)
CREATE TABLE IF NOT EXISTS payment (
	   type VARCHAR(256),
	   date VARCHAR(256),
	   txn_id INT,
	   total VARCHAR(256),
	   status VARCHAR(256)
)
