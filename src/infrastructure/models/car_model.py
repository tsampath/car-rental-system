from sqlalchemy import Column, String, DateTime, BINARY, Integer, Boolean
from sqlalchemy.sql import func

from .base_model import BaseModel
from .base import Base

class CarModel(BaseModel, Base):
    """Car database model."""
    __tablename__ = "car"

    car_id = Column(String(50), nullable=False)
    make = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    mileage = Column(Integer, nullable=False)
    availability = Column(Boolean, nullable=False)
    minimum_rent_period = Column(Integer, nullable=False)
    maximum_rent_period = Column(Integer, nullable=False)    
