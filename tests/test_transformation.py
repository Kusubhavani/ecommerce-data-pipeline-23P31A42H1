from sqlalchemy import text
from config.database import engine

def test_no_orphan_customers():
    query = """
    SELECT COUNT(*)
    FROM orders o
    LEFT JOIN dim_customer c
        ON o.customer_id = c.customer_id
    WHERE c.customer_id IS NULL
    """

    with engine.connect() as conn:
        orphans = conn.execute(text(query)).scalar()

    assert orphans == 0
