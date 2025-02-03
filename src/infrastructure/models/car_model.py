from sqlalchemy import Column, String, Integer, Boolean,DECIMAL
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

from .base_model import BaseModel
from .base import Base

Base = declarative_base()

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
    rate_per_day =  Column(DECIMAL(15, 2), nullable=True)
