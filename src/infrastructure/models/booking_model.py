from sqlalchemy import Column, Integer, ForeignKey, Boolean, DateTime, String, func, DECIMAL
from sqlalchemy.ext.declarative import declarative_base

from .base_model import BaseModel
# from .base import Base
from .car_model import CarModel
from .customer_model import CustomerModel

Base = declarative_base()

class BookingModel(BaseModel, Base):
    """Booking database model."""

    __tablename__ = "booking"

    car_id = Column(Integer, ForeignKey(CarModel.id, ondelete="CASCADE"), nullable=False)
    customer_id = Column(Integer, ForeignKey(CustomerModel.id, ondelete="CASCADE"), nullable=False)
    booking_start_date = Column(DateTime, nullable=False)
    booking_end_date = Column(DateTime, nullable=False)
    is_closed = Column(Boolean, default=False)
    closed_date = Column(DateTime, nullable=True)
    additional_comment = Column(String(1000), nullable=True)
    status_id = Column(Integer, nullable=True)
    total_cost =  Column(DECIMAL(15, 2), nullable=True)
