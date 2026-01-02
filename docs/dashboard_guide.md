# E-Commerce Analytics Dashboard – User Guide

## Overview
This guide explains how to access and use the **E-Commerce Analytics Dashboard**
built on top of the warehouse data model.

The dashboard provides actionable business insights through interactive
visualizations and filters.

---

## Accessing the Dashboard

### Power BI
- File: `dashboards/powerbi/ecommerce_analytics.pbix`
- Requirement: Power BI Desktop (Free)

### Tableau Public
- URL: (Add your published Tableau Public link here)

---

## Dashboard Pages

### Page 1: Executive Summary
**Purpose:** High-level business overview

**Key Metrics:**
- Total Revenue
- Total Transactions
- Average Order Value
- Profit Margin

**Visualizations:**
- Monthly Revenue Trend
- Top Product Categories
- Payment Method Distribution
- Geographic Sales Map

**Usage:**
- Apply date filters to view specific periods
- Click categories to drill down

---

### Page 2: Product Analysis
**Purpose:** Analyze product performance

**Insights:**
- Top products by revenue
- Category-wise profit margin
- Low-performing products
- Pricing impact on sales

---

### Page 3: Customer Insights
**Purpose:** Understand customer behavior

**Insights:**
- High-value (VIP) customers
- Customer contribution to revenue
- Repeat purchase patterns
- Customer segmentation

---

### Page 4: Geographic & Trend Analysis
**Purpose:** Location and time-based patterns

**Insights:**
- Top-performing regions
- State-wise sales distribution
- Weekday vs weekend trends
- Seasonal demand patterns

---

## Filters Available
- Date range
- Product category
- Customer location
- Payment method

---

## Refreshing the Dashboard
1. Run the full pipeline
2. Ensure warehouse tables are updated
3. Refresh dataset in Power BI / Tableau

---

## Key Metrics Definitions
- Revenue: Sum of sales amount
- AOV: Average order value per transaction
- Profit Margin: (Revenue - Cost) / Revenue
- Retention Rate: Repeat customers / Total customers

---

## Business Insights & Recommendations
- Focus on top-performing categories
- Target high-value customers with loyalty programs
- Optimize weekend promotions
- Improve underperforming regions

---

## Troubleshooting
- If dashboard shows no data:
  - Check warehouse tables
  - Verify database connection
  - Re-run pipeline

---

## Conclusion
This dashboard empowers stakeholders to make
data-driven decisions using clean, reliable,
and analytics-ready data.
