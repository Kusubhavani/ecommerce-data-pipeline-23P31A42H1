from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP
from sqlalchemy.sql import func
from models.base import Base

class Product(Base):
    __tablename__ = "products"
    __table_args__ = {"schema": "ecommerce"}

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(150), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    stock = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
