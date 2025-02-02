from datetime import datetime
from typing import Optional

from domain.entities.base_entity import BaseEntity

class BookingEntity(BaseEntity):
    """Pydantic entity for Booking."""

    car_id: int
    customer_id: int
    booking_start_date: datetime
    booking_end_date: datetime
    is_closed: bool = False
    closed_date: Optional[datetime] = None
    additional_comment: Optional[str] = None
    status_id: int

