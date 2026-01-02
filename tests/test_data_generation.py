import os
import pandas as pd

# UPDATE THIS PATH TO MATCH YOUR PROJECT
DATA_PATH = "data"

def find_csv(filename):
    """
    Search recursively for CSV file inside data/
    """
    for root, _, files in os.walk(DATA_PATH):
        if filename in files:
            return os.path.join(root, filename)
    return None


def test_orders_csv_exists():
    path = find_csv("orders.csv")
    assert path is not None, "orders.csv not generated anywhere under data/"


def test_orders_schema_and_nulls():
    path = find_csv("orders.csv")
    assert path is not None, "orders.csv not found"

    df = pd.read_csv(path)

    required_columns = [
        "order_id",
        "customer_id",
        "product_id",
        "quantity",
        "price",
        "order_date",
        "order_status"
    ]

    for col in required_columns:
        assert col in df.columns, f"{col} missing in orders.csv"

    assert df["order_id"].isnull().sum() == 0
    assert df["customer_id"].isnull().sum() == 0
    assert df["product_id"].isnull().sum() == 0
