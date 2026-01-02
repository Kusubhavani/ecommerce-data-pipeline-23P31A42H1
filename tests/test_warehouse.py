from sqlalchemy import inspect
from config.database import engine

def test_fact_and_dimension_tables_exist():
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    assert "fact_orders" in tables
    assert "dim_customer" in tables
    assert "dim_product" in tables
    assert "dim_status" in tables
