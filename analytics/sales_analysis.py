from sqlalchemy import text
import pandas as pd
from config.database import engine

def run_analysis():
    with engine.connect() as conn:
        # Total revenue
        revenue_df = pd.read_sql(
            text("SELECT SUM(total_amount) AS total_revenue FROM orders"),
            conn
        )

        # Orders by status
        status_df = pd.read_sql(
            text("""
                SELECT status, COUNT(*) AS total_orders
                FROM orders
                GROUP BY status
            """),
            conn
        )

        # Top customers
        customers_df = pd.read_sql(
            text("""
                SELECT customer_id, SUM(total_amount) AS total_spent
                FROM orders
                GROUP BY customer_id
                ORDER BY total_spent DESC
                LIMIT 5
            """),
            conn
        )

        print("\n📊 TOTAL REVENUE")
        print(revenue_df)

        print("\n📦 ORDERS BY STATUS")
        print(status_df)

        print("\n👥 TOP 5 CUSTOMERS")
        print(customers_df)

if __name__ == "__main__":
    run_analysis()
