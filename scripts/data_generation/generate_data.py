import pandas as pd
import random
from datetime import datetime, timedelta

# Number of records to generate
NUM_RECORDS = 500

def generate_orders():
    orders = []

    for i in range(1, NUM_RECORDS + 1):
        order = {
            "order_id": i,
            "customer_id": random.randint(1000, 1100),
            "product_id": random.randint(200, 250),
            "quantity": random.randint(1, 5),
            "price": round(random.uniform(100, 1000), 2),
            "order_date": (
                datetime.now() - timedelta(days=random.randint(1, 30))
            ).strftime("%Y-%m-%d"),
            "order_status": random.choice(
                ["PLACED", "SHIPPED", "DELIVERED", "CANCELLED"]
            ),
        }
        orders.append(order)

    return orders


def main():
    orders = generate_orders()
    df = pd.DataFrame(orders)

    # Save to CSV
    df.to_csv("data/orders.csv", index=False)
    print("✅ orders.csv generated successfully in data/ folder")


if __name__ == "__main__":
    main()
