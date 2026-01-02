from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from models.base import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "ecommerce"}

    user_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
