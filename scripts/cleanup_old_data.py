# scripts/cleanup_old_data.py

import os
import time
import logging
from datetime import datetime, timedelta

# Configuration
RETENTION_DAYS = 7
TARGET_DIRS = [
    "data/raw",
    "data/staging",
    "logs"
]

PRESERVE_KEYWORDS = ["summary", "report", "metadata"]

LOG_FILE = "logs/scheduler_activity.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def should_preserve(file_name):
    return any(keyword in file_name.lower() for keyword in PRESERVE_KEYWORDS)

def cleanup_old_files():
    logging.info("Starting cleanup process")

    cutoff_time = time.time() - (RETENTION_DAYS * 86400)
    today = datetime.today().date()

    deleted_files = 0

    for directory in TARGET_DIRS:
        if not os.path.exists(directory):
            continue

        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)

                # Preserve summary / report / metadata
                if should_preserve(file):
                    continue

                # Preserve today's files
                file_mtime = os.path.getmtime(file_path)
                file_date = datetime.fromtimestamp(file_mtime).date()
                if file_date == today:
                    continue

                # Delete old files
                if file_mtime < cutoff_time:
                    try:
                        os.remove(file_path)
                        deleted_files += 1
                        logging.info(f"Deleted old file: {file_path}")
                    except Exception as e:
                        logging.error(f"Failed to delete {file_path}: {e}")

    logging.info(f"Cleanup completed. Files deleted: {deleted_files}")

if __name__ == "__main__":
    cleanup_old_files()
