from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.sql import func
from .base_model import BaseModel

class UserModel(BaseModel):
    """User database model."""
    __tablename__ = "user"
 
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    dob = Column(DateTime, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
