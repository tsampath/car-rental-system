from domain.entities.base_entity import BaseEntity
from datetime import datetime
from typing import Optional

class CarEntity(BaseEntity):
    """User DTO with Pydantic validation."""
    car_id: str
    make: str
    model: str
    year: int
    mileage: int
    availability: bool
    minimum_rent_period: int
    maximum_rent_period: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
