from typing import Optional
from datetime import datetime

from domain.entities.base_entity import BaseEntity

class CustomerEntity(BaseEntity):
    """Customer DTO with Pydantic validation."""
    name: str
    building_name: str
    address_line_1: str
    address_line_2: str
    town: str
    customer_type_id: int
    price_list_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
