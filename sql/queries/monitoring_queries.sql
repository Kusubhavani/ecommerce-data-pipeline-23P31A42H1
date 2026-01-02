/* =========================
   1. DATA FRESHNESS CHECK
   ========================= */

-- Staging freshness
SELECT MAX(loaded_at) AS staging_latest
FROM staging_orders;

-- Production freshness
SELECT MAX(order_date) AS production_latest
FROM orders;

-- Warehouse freshness
SELECT MAX(order_date) AS warehouse_latest
FROM fact_sales;


/* =========================
   2. DATA VOLUME (30 DAYS)
   ========================= */

SELECT
    order_date::date AS day,
    COUNT(*) AS daily_count
FROM orders
WHERE order_date >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY order_date::date
ORDER BY day;


/* =========================
   3. DATA QUALITY CHECKS
   ========================= */

-- Null checks
SELECT COUNT(*) AS null_violations
FROM orders
WHERE customer_id IS NULL
   OR product_id IS NULL
   OR quantity IS NULL
   OR total_amount IS NULL;

-- Orphan records (example)
SELECT COUNT(*) AS orphan_orders
FROM orders o
LEFT JOIN dim_customers c ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;


/* =========================
   4. DATABASE HEALTH
   ========================= */

-- Active connections
SELECT COUNT(*) AS active_connections
FROM pg_stat_activity
WHERE state = 'active';
