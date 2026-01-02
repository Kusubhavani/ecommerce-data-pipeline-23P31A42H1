from config.database import engine
from sqlalchemy import text

def create_orders_table():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS orders (
        order_id INT PRIMARY KEY,
        customer_id INT,
        product_id INT,
        quantity INT,
        total_amount NUMERIC(10, 2),
        order_date DATE,
        status VARCHAR(20)
    );
    """

    with engine.connect() as conn:
        conn.execute(text(create_table_query))
        conn.commit()

    print("✅ Orders table created successfully")

if __name__ == "__main__":
    create_orders_table()
