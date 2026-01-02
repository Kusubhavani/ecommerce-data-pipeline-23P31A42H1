import schedule
import subprocess
import time
import sys
import logging
from pathlib import Path

# ---------------- PATHS ----------------
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

# ---------------- LOGGING ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "scheduler_activity.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

LOCK_FILE = BASE_DIR / "pipeline.lock"


# ---------------- PIPELINE JOB ----------------
def run_pipeline_job():
    if LOCK_FILE.exists():
        logger.warning("Pipeline already running. Skipping this run.")
        return

    try:
        LOCK_FILE.touch()
        logger.info("Triggering pipeline execution")

        subprocess.run(
            [sys.executable, str(BASE_DIR / "scripts" / "pipeline_orchestrator.py")],
            check=True
        )

        logger.info("Pipeline execution completed")

    except Exception as e:
        logger.error(f"Pipeline execution failed: {e}")

    finally:
        if LOCK_FILE.exists():
            LOCK_FILE.unlink()


# ---------------- SCHEDULER ----------------
def main():
    logger.info("Scheduler started (TEST MODE: every 15 seconds)")
    schedule.every(15).seconds.do(run_pipeline_job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
