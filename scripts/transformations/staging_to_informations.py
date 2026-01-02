import logging
from sqlalchemy import text
from config.database import engine

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def load_staging_to_information():
    logging.info("Starting staging → information transformation")

    with engine.begin() as conn:
        logging.info("Truncating orders table")
        conn.execute(text("TRUNCATE TABLE orders RESTART IDENTITY CASCADE;"))

        insert_sql = """
        INSERT INTO orders (
            order_id,
            customer_id,
            product_id,
            quantity,
            total_amount,
            order_date,
            status
        )
        SELECT
            order_id,
            customer_id,
            product_id,
            quantity,
            total_amount,
            order_date,
            status
        FROM staging_orders;
        """

        conn.execute(text(insert_sql))
        logging.info("Orders table loaded successfully")

    logging.info("Staging → information transformation completed")

if __name__ == "__main__":
    load_staging_to_information()
