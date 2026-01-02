# E-Commerce Data Pipeline – Architecture Documentation

## Overview
This document describes the architecture of the **E-Commerce Data Pipeline**.
The system is designed to handle the full data lifecycle from raw data generation
to analytics-ready datasets and BI dashboards.

The architecture follows **layered data modeling**, **separation of concerns**,
and **scalable data engineering principles**.

---

## System Components

### 1. Data Generation Layer
- Generates synthetic e-commerce data using **Python Faker**
- Produces CSV files:
  - customers
  - products
  - orders
  - order_items
- Ensures referential integrity at source level

**Output:** Raw CSV files stored in `data/raw/`

---

### 2. Data Ingestion Layer
- Loads raw CSV data into PostgreSQL staging schema
- Uses Python + Pandas + SQLAlchemy
- Implements transactional loading with rollback on failure

**Schema:** `staging`  
**Pattern:** Batch ingestion

---

### 3. Data Storage Layer

#### Staging Schema
- Exact replica of raw CSV structure
- Minimal validation
- Temporary storage for ingestion

#### Production Schema
- Cleaned and normalized (3NF)
- Enforces:
  - Primary keys
  - Foreign keys
  - Data constraints
- Removes duplicates and invalid records

#### Warehouse Schema
- Dimensional model (Star Schema)
- Optimized for analytical queries
- Contains facts and dimensions

---

### 4. Data Processing Layer
- Applies data transformations:
  - Cleansing
  - Normalization
  - Enrichment
- Implements:
  - Data quality checks
  - Business rules
  - Surrogate keys
  - SCD Type 2 for dimensions
- Builds aggregate tables for performance

---

### 5. Data Serving Layer
- Pre-computed analytical tables
- Optimized SQL queries
- Supports BI tools directly

---

### 6. Visualization Layer
- Power BI Desktop
- Tableau Public
- Interactive dashboards with filters and drill-downs
- Business-focused KPIs and trends

---

### 7. Orchestration Layer
- Pipeline orchestrator coordinates all steps
- Scheduler triggers pipeline execution
- Monitoring detects anomalies and failures
- Cleanup jobs manage old data

---

## Data Models

### Staging Model
- One-to-one mapping with CSV files
- No transformations
- Used only as intermediate storage

---

### Production Model
- 3NF normalized structure
- Strong referential integrity
- Business rules enforced
- Serves as trusted source of truth

---

### Warehouse Model (Star Schema)
- Dimension tables:
  - dim_customer
  - dim_product
  - dim_date
  - dim_status
- Fact table:
  - fact_sales
- Aggregate tables for performance

---

## Technology Choices & Rationale

- **PostgreSQL**: Reliable, ACID-compliant analytical database
- **Star Schema**: Optimized for BI queries
- **Python**: Flexibility and ecosystem support
- **SQLAlchemy**: Safe and reusable DB access
- **Pytest**: Automated quality assurance

---

## Deployment Architecture
- Local deployment using Python virtual environment
- Docker-ready structure for future containerization
- Supports cloud migration without major redesign

---

## Design Decisions & Trade-offs
- Batch processing chosen over streaming for simplicity
- JSON-based monitoring for lightweight alerting
- Aggregates used to reduce BI query latency

---

## Conclusion
This architecture provides a robust, scalable, and production-ready
foundation for e-commerce analytics while maintaining simplicity
for academic evaluation.
