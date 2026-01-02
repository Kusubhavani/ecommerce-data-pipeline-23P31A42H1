import json
import time
from datetime import datetime, date, timezone
from sqlalchemy import text
from config.database import engine

PIPELINE_REPORT = "data/processed/pipeline_execution_report.json"
MONITORING_REPORT = "data/processed/monitoring_report.json"


# -----------------------------
# Utilities
# -----------------------------
def utc_now():
    return datetime.now(timezone.utc)


def make_utc(dt):
    if dt is None:
        return None

    if isinstance(dt, date) and not isinstance(dt, datetime):
        return datetime(dt.year, dt.month, dt.day, tzinfo=timezone.utc)

    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)

    return dt.astimezone(timezone.utc)


# -----------------------------
# Checks
# -----------------------------
def check_last_execution(alerts):
    if not os.path.exists(PIPELINE_REPORT):
        alerts.append({
            "severity": "critical",
            "check": "last_execution",
            "message": "pipeline_execution_report.json not found",
            "timestamp": utc_now().isoformat()
        })
        return {"status": "critical"}

    with open(PIPELINE_REPORT, "r") as f:
        report = json.load(f)

    last_run = make_utc(datetime.fromisoformat(report["end_time"]))
    hours_since = (utc_now() - last_run).total_seconds() / 3600

    status = "ok"
    if hours_since > 25:
        status = "critical"
        alerts.append({
            "severity": "critical",
            "check": "last_execution",
            "message": f"No run in {hours_since:.2f} hours",
            "timestamp": utc_now().isoformat()
        })

    return {
        "status": status,
        "last_run": last_run.isoformat(),
        "hours_since_last_run": round(hours_since, 2),
        "threshold_hours": 25
    }


def check_data_freshness(alerts):
    query = "SELECT MAX(order_date) FROM orders;"
    with engine.connect() as conn:
        latest = conn.execute(text(query)).scalar()

    latest = make_utc(latest)
    lag_hours = (utc_now() - latest).total_seconds() / 3600 if latest else None

    status = "ok"
    if lag_hours and lag_hours > 24:
        status = "warning"

    return {
        "status": status,
        "latest_record": latest.isoformat() if latest else None,
        "lag_hours": round(lag_hours, 2) if lag_hours else None
    }


def check_data_volume(alerts):
    query = "SELECT COUNT(*) FROM orders WHERE order_date = CURRENT_DATE;"
    with engine.connect() as conn:
        count_today = conn.execute(text(query)).scalar()

    anomaly = count_today == 0
    if anomaly:
        alerts.append({
            "severity": "warning",
            "check": "data_volume",
            "message": "Zero records today",
            "timestamp": utc_now().isoformat()
        })

    return {
        "status": "anomaly_detected" if anomaly else "ok",
        "records_today": count_today,
        "anomaly_detected": anomaly
    }


def check_data_quality(alerts):
    query = """
        SELECT COUNT(*) FROM orders
        WHERE order_id IS NULL
           OR customer_id IS NULL
           OR product_id IS NULL
           OR total_amount IS NULL;
    """
    with engine.connect() as conn:
        violations = conn.execute(text(query)).scalar()

    status = "ok" if violations == 0 else "degraded"
    return {
        "status": status,
        "null_violations": violations
    }


def check_database_health(alerts):
    start = time.time()
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        response = (time.time() - start) * 1000
        return {
            "status": "ok",
            "response_time_ms": round(response, 2)
        }
    except Exception:
        alerts.append({
            "severity": "critical",
            "check": "database_connectivity",
            "message": "Database unreachable",
            "timestamp": utc_now().isoformat()
        })
        return {"status": "error"}


# -----------------------------
# Main
# -----------------------------
def run_monitoring():
    alerts = []

    report = {
        "monitoring_timestamp": utc_now().isoformat(),
        "checks": {},
        "alerts": alerts
    }

    report["checks"]["last_execution"] = check_last_execution(alerts)
    report["checks"]["data_freshness"] = check_data_freshness(alerts)
    report["checks"]["data_volume"] = check_data_volume(alerts)
    report["checks"]["data_quality"] = check_data_quality(alerts)
    report["checks"]["database_connectivity"] = check_database_health(alerts)

    if any(a["severity"] == "critical" for a in alerts):
        report["pipeline_health"] = "critical"
        report["overall_health_score"] = 40
    elif alerts:
        report["pipeline_health"] = "degraded"
        report["overall_health_score"] = 75
    else:
        report["pipeline_health"] = "healthy"
        report["overall_health_score"] = 100

    with open(MONITORING_REPORT, "w") as f:
        json.dump(report, f, indent=4)

    print("Monitoring report generated successfully")


if __name__ == "__main__":
    import os
    run_monitoring()
