-- ============================
-- WAREHOUSE SCHEMA
-- ============================

CREATE SCHEMA IF NOT EXISTS warehouse;

-- ============================
-- BASE ORDERS TABLE (FOR TESTS)
-- ============================

DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    order_id VARCHAR(20),
    customer_id VARCHAR(20),
    product_id VARCHAR(20),
    status VARCHAR(50),
    order_date DATE,
    total_amount DECIMAL(12,2)
);

-- ============================
-- DIMENSION TABLES
-- ============================

DROP TABLE IF EXISTS dim_customer;

CREATE TABLE dim_customer (
    customer_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(200),
    email VARCHAR(150),
    city VARCHAR(100)
);

DROP TABLE IF EXISTS dim_product;

CREATE TABLE dim_product (
    product_id VARCHAR(20) PRIMARY KEY,
    product_name VARCHAR(200),
    category VARCHAR(100),
    price DECIMAL(10,2)
);

DROP TABLE IF EXISTS dim_status;

CREATE TABLE dim_status (
    status_id SERIAL PRIMARY KEY,
    status VARCHAR(50) UNIQUE
);

-- ============================
-- FACT TABLE
-- ============================

DROP TABLE IF EXISTS fact_orders;

CREATE TABLE fact_orders (
    order_id VARCHAR(20),
    customer_id VARCHAR(20),
    product_id VARCHAR(20),
    status VARCHAR(50),
    order_date DATE,
    total_amount DECIMAL(12,2)
);
