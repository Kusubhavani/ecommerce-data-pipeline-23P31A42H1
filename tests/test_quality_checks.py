import os
import json

REPORT_PATH = "data/processed/pipeline_execution_report.json"

def test_quality_report_exists():
    assert os.path.exists(REPORT_PATH)

def test_quality_score_present():
    with open(REPORT_PATH) as f:
        report = json.load(f)

    assert "status" in report
    assert "steps_executed" in report
