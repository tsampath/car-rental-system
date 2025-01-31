from sqlalchemy import Column, Integer, ForeignKey, Boolean, DateTime, String, func

from infrastructure.models.base_model import BaseModel
from infrastructure.models.car_model import CarModel
from infrastructure.models.customer_model import CustomerModel

class BookingModel(BaseModel):
    """Booking database model."""

    __tablename__ = "booking"

    car_id = Column(Integer, ForeignKey(CarModel.id, ondelete="CASCADE"), nullable=False)
    customer_id = Column(Integer, ForeignKey(CustomerModel.id, ondelete="CASCADE"), nullable=False)
    booking_start_date = Column(DateTime, nullable=False)
    booking_end_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    is_closed = Column(Boolean, default=False)
    closed_date = Column(DateTime, nullable=True)
    additional_comment = Column(String(1000), nullable=True)

