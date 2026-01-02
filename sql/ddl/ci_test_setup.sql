-- ======================================
-- CI TEST DATABASE SETUP (FINAL VERSION)
-- ======================================

-- Ensure schemas exist
CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS production;
CREATE SCHEMA IF NOT EXISTS warehouse;

-- -------------------------
-- PRODUCTION-LIKE TABLES
-- -------------------------
DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    order_id VARCHAR(20),
    customer_id VARCHAR(20),
    status VARCHAR(50)
);

-- -------------------------
-- DIMENSION TABLES
-- -------------------------
DROP TABLE IF EXISTS dim_customer;
CREATE TABLE dim_customer (
    customer_id VARCHAR(20),
    customer_name TEXT
);

DROP TABLE IF EXISTS dim_product;
CREATE TABLE dim_product (
    product_id VARCHAR(20),
    product_name TEXT
);

DROP TABLE IF EXISTS dim_status;
CREATE TABLE dim_status (
    status VARCHAR(50),
    status_description TEXT
);

-- -------------------------
-- FACT TABLE
-- -------------------------
DROP TABLE IF EXISTS fact_orders;
CREATE TABLE fact_orders (
    order_id VARCHAR(20),
    customer_id VARCHAR(20),
    product_id VARCHAR(20),
    status VARCHAR(50)
);

-- -------------------------
-- MINIMAL TEST DATA
-- -------------------------
INSERT INTO dim_customer VALUES ('C001', 'Test Customer');
INSERT INTO dim_product VALUES ('P001', 'Test Product');
INSERT INTO dim_status VALUES ('DELIVERED', 'Delivered Successfully');

INSERT INTO orders VALUES ('O001', 'C001', 'DELIVERED');
INSERT INTO fact_orders VALUES ('O001', 'C001', 'P001', 'DELIVERED');
