from sqlalchemy import Column, String, DateTime, BINARY, Integer, Boolean, Sequence
from sqlalchemy.sql import func
from .base_model import BaseModel

class CustomerModel(BaseModel):
    """Customer database model."""
    __tablename__ = "customer"

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_auto_increment': '1000'  # Auto-increment initial value
    }
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    building_name = Column(String(50), nullable=True)
    address_line_1 = Column(String(50), nullable=True)
    address_line_2 = Column(String(50), nullable=True)
    town = Column(String(50), nullable=True)
    customer_type_id = Column(Integer, nullable=False)
    price_list_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
