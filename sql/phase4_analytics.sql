-- PHASE 4.1: ANALYTICS QUERIES

-- Q1 Total Revenue
SELECT SUM(total_amount) AS total_revenue FROM fact_orders;

-- Q2 Total Orders
SELECT COUNT(*) AS total_orders FROM fact_orders;

-- Q3 Revenue by Status
SELECT status, SUM(total_amount) AS revenue
FROM fact_orders
GROUP BY status;

-- (keep adding ALL queries…)

-- ADVANCED SQL

-- Window Function
SELECT customer_id,
       SUM(total_amount) AS total_spent,
       RANK() OVER (ORDER BY SUM(total_amount) DESC) AS rank
FROM fact_orders
GROUP BY customer_id;
