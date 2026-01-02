import subprocess
import sys
import time
import json
import logging
from datetime import datetime
from pathlib import Path

# ---------------- PATHS ----------------
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
REPORT_DIR = BASE_DIR / "data" / "processed"

LOG_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

# ---------------- LOGGING ----------------
log_file = LOG_DIR / f"pipeline_orchestrator_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# ---------------- PIPELINE STEPS ----------------
PIPELINE_STEPS = [
    (
        "Data Quality Checks",
        [sys.executable, "-m", "scripts.quality_checks.data_quality_checks"]
    ),
    (
        "Staging to Production",
        [sys.executable, "-m", "scripts.transformations.staging_to_informations"]
    )
]

MAX_RETRIES = 3
BACKOFF = [1, 2, 4]


# ---------------- PIPELINE RUNNER ----------------
def run_pipeline():
    logger.info("PIPELINE STARTED")

    report = {
        "pipeline_execution_id": f"PIPE_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        "start_time": datetime.utcnow().isoformat(),
        "steps_executed": {},
        "status": "success",
        "errors": []
    }

    for step_name, command in PIPELINE_STEPS:
        success = False

        for attempt in range(MAX_RETRIES):
            try:
                logger.info(f"Starting step: {step_name} (Attempt {attempt + 1})")
                start = time.time()

                subprocess.run(command, check=True)

                duration = round(time.time() - start, 2)
                report["steps_executed"][step_name] = {
                    "status": "success",
                    "duration_seconds": duration,
                    "retry_attempts": attempt
                }

                success = True
                break

            except Exception as e:
                logger.error(f"{step_name} failed: {e}")
                if attempt < MAX_RETRIES - 1:
                    time.sleep(BACKOFF[attempt])
                else:
                    report["steps_executed"][step_name] = {
                        "status": "failed",
                        "error_message": str(e),
                        "retry_attempts": attempt + 1
                    }
                    report["status"] = "failed"
                    report["errors"].append(str(e))
                    logger.info("PIPELINE FINISHED")
                    save_report(report)
                    return

    report["end_time"] = datetime.utcnow().isoformat()
    logger.info("PIPELINE FINISHED")
    save_report(report)


def save_report(report):
    path = REPORT_DIR / "pipeline_execution_report.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)
    logger.info(f"Execution report saved to {path}")


if __name__ == "__main__":
    run_pipeline()
