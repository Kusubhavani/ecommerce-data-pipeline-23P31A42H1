# Docker Deployment Guide – Ecommerce Data Pipeline

This document explains how to deploy, run, and manage the Ecommerce Data Pipeline
using Docker and Docker Compose.

------------------------------------------------
## 1. Prerequisites
------------------------------------------------

### Docker Requirements:
- Docker version 20.10 or higher
- Docker Compose version 2.0 or higher

### Verify installation:
docker --version
docker compose version

### System Requirements:
- Minimum 4 GB RAM
- Minimum 10 GB free disk space
- Supported OS:
  - Linux
  - macOS
  - Windows (WSL2 recommended)

------------------------------------------------
## 2. Quick Start Guide
------------------------------------------------

Step 1: Build Docker Images
docker compose build

Step 2: Start All Services
docker compose up -d

This starts:
- PostgreSQL database service
- Data pipeline service

Step 3: Verify Services Are Running
docker compose ps

Expected:
- postgres service shows healthy
- pipeline service is running

Step 4: Run the Data Pipeline
The pipeline waits for the database health check automatically.

To run manually:
docker compose exec pipeline python scripts/pipeline_orchestrator.py

Step 5: Access PostgreSQL Database
docker compose exec postgres psql -U test_user -d ecommerce_db_test

Step 6: View Logs
docker compose logs pipeline
docker compose logs postgres

Step 7: Stop Services
docker compose down

Step 8: Clean Up (Remove Volumes and Images)
WARNING: This deletes all persisted data

docker compose down -v
docker system prune -f

------------------------------------------------
## 3. Configuration
------------------------------------------------

### Environment Variables:
Configured in docker-compose.yml

- DB_HOST=postgres
- DB_PORT=5432
- DB_NAME=ecommerce_db_test
- DB_USER=test_user
- DB_PASSWORD=test_password

Volume Mounts:
- postgres_data → PostgreSQL persistent storage
- ./data → Pipeline generated files
- ./logs → Pipeline logs

Network Configuration:
- Uses Docker bridge network
- Services communicate using service names
- No hardcoded IP addresses

Resource Limits:
Pipeline container limits:
- CPU: 0.5 cores
- Memory: 512 MB

------------------------------------------------
##  4. Troubleshooting
------------------------------------------------

### Port Already in Use:
Error:
bind: address already in use

Solution:
- Stop local PostgreSQL service
- Or change exposed port in docker-compose.yml

### Database Not Ready:
Cause:
Pipeline starts before database

Solution:
- Healthcheck configured for PostgreSQL
- depends_on with condition service_healthy

### Volume Permission Issues:
Error:
Permission denied

Solution:
sudo chown -R $USER:$USER data logs

### Container Fails to Start:
Check logs:
docker compose logs pipeline

Network Connectivity Issues:
Ensure:
- DB_HOST is set to postgres
- Services are on the same Docker network

------------------------------------------------
### 5. Data Persistence Verification
------------------------------------------------

Step 1: Stop containers
docker compose down

Step 2: Restart containers
docker compose up -d

Result:
- Database tables persist
- Pipeline outputs persist
- Logs persist across restarts

------------------------------------------------
## Conclusion
------------------------------------------------

This Docker deployment ensures:
- Proper service isolation
- Reliable dependency management
- Health-checked startup
- Persistent data storage
- Reproducible pipeline execution
