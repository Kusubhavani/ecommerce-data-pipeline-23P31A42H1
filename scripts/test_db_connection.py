from config.database import engine
from sqlalchemy import text

def test_connection():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT current_database();"))
        for row in result:
            print("Connected to database:", row[0])

if __name__ == "__main__":
    test_connection()
