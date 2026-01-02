# 📦 Project Submission – E-Commerce Data Pipeline

---

## 👩‍🎓 Student Information

- **Name:** Kusu Bhavani  
- **Roll Number:** 23P31A42H1 
- **Email:** bhavanikusu92@gmail.com  
- **Submission Date:** 02-01-2026  

---

## 🔗 GitHub Repository

- **Repository URL:**  
  https://github.com/Kusubhavani/ecommerce-data-pipeline-23P31A42H1  

- **Repository Status:** Public  
- **Branch:** main  
- **Commit Count:** (check from GitHub → Commits tab)

---

## ✅ Project Completion Status

### Phase 1: Setup (8 points)
- ✔ Repository structure created  
- ✔ Environment setup documented  
- ✔ Dependencies configured  
- ✔ Docker configuration completed  

### Phase 2: Data Generation & Ingestion (18 points)
- ✔ Data generation scripts implemented  
- ✔ PostgreSQL schemas created  
- ✔ Data ingestion completed  

### Phase 3: Transformation & Processing (22 points)
- ✔ Data quality checks implemented  
- ✔ Staging → Production ETL  
- ✔ Data warehouse (Star Schema) completed  

### Phase 4: Analytics & BI (18 points)
- ✔ Analytical SQL queries written  
- ✔ BI dashboard created  

### Phase 5: Automation (14 points)
- ✔ Pipeline orchestrator implemented  
- ✔ Scheduling configured  
- ✔ Monitoring & alerting implemented  

### Phase 6: Testing & Documentation (12 points)
- ✔ Unit tests written  
- ✔ Comprehensive documentation completed  

### Phase 7: Deployment (8 points)
- ✔ CI/CD pipeline implemented  
- ✔ Docker deployment verified  
- ✔ Final submission prepared  

---

## 📊 Dashboard Links

- **Power BI Dashboard:**  
  See screenshots under `dashboards/screenshots/`

- **Tableau Public (if applicable):**  
  (Add URL here if used)

---

## 📁 Key Deliverables

- ✔ Complete source code in GitHub  
- ✔ SQL scripts for all schemas  
- ✔ Python scripts for the entire pipeline  
- ✔ BI dashboard (Power BI / Tableau)  
- ✔ Unit tests with required coverage  
- ✔ End-to-end documentation  

---

## ▶ Running Instructions

### Clone Repository
```bash
git clone https://github.com/Kusubhavani/ecommerce-data-pipeline-23P31A42H1
cd ecommerce-data-pipeline-23P31A42H1
```
---

### SetUp Environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
---

### Run Pipeline
```bash
python scripts/pipeline_orchestrator.py
```
---

### Run Tests
```bash
pytest tests/ -v
```
---
## Project Statistics

 Total Lines of Code: ~3000+

 Total Data Records Generated: 30,000+

 Dashboard Visualizations: 16+

 Test Coverage: Automated via CI

---

## Challenges Faced

### 1.Schema Alignment Issues
Solved by strictly following naming conventions and schema separation.

### 2.CI/CD Database Connectivity Errors
Solved by configuring PostgreSQL service containers with health checks.

### 3.Warehouse Table Dependencies
Solved by enforcing correct ETL execution order and validations.

---

## Declaration

I hereby declare that this project is my original work and has been completed independently.
All resources used are for learning purposes, and no part of this project is plagiarized.

Signature: Bhavani Kusu
Date: 02-01-2026

---

## Submission Steps 
```bash
git add .
git commit -m "Final submission"
git push origin main

git tag -a v1.0 -m "Final Submission"
git push origin v1.0
```

---

## Final Steps

Repository is public and complete

All required files are committed

.gitignore properly configured

Docker, CI/CD, and documentation verified
