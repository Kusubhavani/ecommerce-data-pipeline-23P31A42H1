import csv
from sqlalchemy import text
from config.database import engine

def load_orders():
    with engine.connect() as conn:
        with open("data/orders.csv", newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                insert_query = text("""
                    INSERT INTO orders (
                        order_id,
                        customer_id,
                        product_id,
                        quantity,
                        total_amount,
                        order_date,
                        status
                    )
                    VALUES (
                        :order_id,
                        :customer_id,
                        :product_id,
                        :quantity,
                        :total_amount,
                        :order_date,
                        :status
                    )
                    ON CONFLICT (order_id) DO NOTHING;
                """)

                conn.execute(insert_query, {
                    "order_id": int(row["order_id"]),
                    "customer_id": int(row["customer_id"]),
                    "product_id": int(row["product_id"]),
                    "quantity": int(row["quantity"]),
                    "total_amount": float(row["price"]),  # ✅ FIX
                    "order_date": row["order_date"],
                    "status": row["order_status"]
                })

        conn.commit()

    print("✅ Orders data loaded successfully")

if __name__ == "__main__":
    load_orders()
