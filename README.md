# E-Commerce Data Pipeline Project

## Project Overview
This project implements an end-to-end **E-Commerce Data Pipeline** following modern **data engineering best practices**.  
It covers the complete lifecycle of data from **generation to analytics**, including ingestion, transformation, data quality checks, monitoring, testing, CI/CD, Docker deployment, and BI dashboards.

The pipeline is **modular, scalable, and production-oriented**, with strong emphasis on **automation, data quality, monitoring, testing, and deployment readiness**.

---

## Project Architecture

### Data Flow

Raw CSV Files  
↓  
Staging Schema (PostgreSQL)  
↓  
Production Schema (Cleaned & Normalized)  
↓  
Warehouse Schema (Star Schema)  
↓  
Analytics & Aggregates  
↓  
BI Dashboards (Power BI / Tableau)

---

## Technology Stack

- **Data Generation:** Python, Faker  
- **Database:** PostgreSQL  
- **ETL / Transformations:** Python, Pandas, SQLAlchemy  
- **Orchestration:** Python Pipeline Orchestrator  
- **Monitoring & Alerting:** Python, JSON-based reports  
- **Testing:** Pytest, Pytest-cov  
- **CI/CD:** GitHub Actions  
- **Containerization:** Docker, Docker Compose  
- **BI Tools:** Power BI Desktop / Tableau Public  
- **Version Control:** Git & GitHub  

---

## Project Structure

```
ecommerce-data-pipeline/
├── config/
│   └── database.py
├── data/
│   ├── raw/
│   ├── processed/
│   └── warehouse/
├── scripts/
│   ├── data_generation/
│   ├── ingestion/
│   ├── transformations/
│   ├── quality_checks/
│   ├── monitoring/
│   ├── scheduler.py
│   ├── pipeline_orchestrator.py
│   └── cleanup_old_data.py
├── sql/
│   ├── ddl/
│   └── queries/
├── tests/
│   ├── test_data_generation.py
│   ├── test_ingestion.py
│   ├── test_transformation.py
│   ├── test_quality_checks.py
│   └── test_warehouse.py
├── dashboards/
│   ├── powerbi/
│   └── screenshots/
├── docker/
│   └── README.md
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   ├── architecture.md
│   └── dashboard_guide.md
├── pytest.ini
├── requirements.txt
├── README.md
└── SUBMISSION.md
```

---

## Setup Instructions

### Prerequisites

- Python 3.10+
- PostgreSQL 14+
- Git
- Docker & Docker Compose
- Power BI Desktop or Tableau Public

---

### Step-by-Step Setup

Clone the repository:

```
git clone https://github.com/Kusubhavani/ecommerce-data-pipeline-23P31A42H1.git
cd ecommerce-data-pipeline-23P31A42H1
```

Create virtual environment:

```
python -m venv venv
```

Activate environment:

```
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Database Setup

- Create a PostgreSQL database
- Update credentials in `config/database.py`
- Verify database connectivity

---

## Running the Pipeline

### Full Pipeline Execution

```
python scripts/pipeline_orchestrator.py
```

---

### Individual Steps

```
python scripts/data_generation/generate_data.py
python scripts/ingestion/ingest_to_staging.py
python scripts/transformations/staging_to_production.py
python scripts/transformations/load_warehouse.py
python scripts/transformations/generate_analytics.py
```

---

## Monitoring & Alerting

### Monitoring Coverage

- Pipeline execution health
- Data freshness
- Data volume anomalies
- Data quality trends
- Database connectivity

Run monitoring:

```
python -m scripts.monitoring.pipeline_monitor
```

Monitoring output:

```
data/processed/monitoring_report.json
```

Alert Levels:
- **Critical:** Pipeline stopped, database unreachable, zero records
- **Warning:** Data delays, volume anomalies, quality degradation

---

## Testing 

Run all tests:

```
pytest
```

Run tests with coverage:

```
pytest --cov=scripts --cov-report=html
```

---

## Database Schemas

### Staging Schema
- staging.customers
- staging.products
- staging.transactions
- staging.transaction_items

### Production Schema
- production.customers
- production.products
- production.transactions
- production.transaction_items

### Warehouse Schema
- warehouse.dim_customer
- warehouse.dim_product
- warehouse.dim_date
- warehouse.dim_status
- warehouse.fact_orders

---

## Analytics & BI Dashboards

- **Power BI:** `dashboards/powerbi/ecommerce_analytics.pbix`
- **Tableau Public:** Add published dashboard URL
- **Screenshots:** `dashboards/screenshots/`

---

## Key Insights from Analytics

- Top product categories drive most revenue
- Weekend sales outperform weekdays
- High-value customers dominate revenue share
- Seasonal sales patterns identified

---

## Challenges & Solutions

- **Pipeline execution time:** Optimized SQL and modular execution  
- **Data quality issues:** Automated quality checks  
- **Monitoring complexity:** Centralized JSON reports  
- **CI test failures:** Proper schema isolation  

---

## Docker & CI/CD

- Dockerized pipeline using Docker Compose
- PostgreSQL service with health checks
- Pipeline waits for DB readiness
- GitHub Actions CI for automated testing
- Docker deployment guide available in `docker/README.md`

---

## Future Enhancements

- Kafka-based real-time streaming
- Cloud deployment (AWS / GCP / Azure)
- ML-based forecasting
- Slack / Email alerts

---

## Contact

**Name:** Kusu Bhavani 
**Roll Number:** 23P31A42H1 
**Email:** bhavanikusu92@gmail.com  
**GitHub:** https://github.com/Kusubhavani 

---

## Acknowledgement

This project was developed as part of an academic **Data Engineering Capstone**, following industry-aligned standards.
