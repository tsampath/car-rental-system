from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

from .customer_model import CustomerModel
from .base_model import BaseModel


Base = declarative_base()

class UserModel(BaseModel, Base):
    """User database model."""
    __tablename__ = "user"
 
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    dob = Column(DateTime, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role_id = Column(Integer, nullable=True, default=2)
    customer_id = Column(Integer, ForeignKey(CustomerModel.id, ondelete="CASCADE"), nullable=True)
