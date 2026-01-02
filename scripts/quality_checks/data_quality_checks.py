# scripts/quality_checks/data_quality_checks.py

from sqlalchemy import text
from config.database import engine

def run_data_quality_checks():
    checks = {
        "null_order_id": """
            SELECT COUNT(*)
            FROM staging_orders
            WHERE order_id IS NULL
        """,

        "negative_total_amount": """
            SELECT COUNT(*)
            FROM staging_orders
            WHERE total_amount < 0
        """,

        "duplicate_order_ids": """
            SELECT COUNT(*) - COUNT(DISTINCT order_id)
            FROM staging_orders
        """,

        "invalid_status": """
            SELECT COUNT(*)
            FROM staging_orders
            WHERE status NOT IN (
                'PLACED', 'SHIPPED', 'DELIVERED', 'CANCELLED'
            )
        """
    }

    with engine.connect() as conn:
        for check_name, query in checks.items():
            result = conn.execute(text(query)).scalar()
            if result > 0:
                raise Exception(f"❌ Data Quality Failed: {check_name}")

    print("✅ Data Quality Checks Passed")

if __name__ == "__main__":
    run_data_quality_checks()
