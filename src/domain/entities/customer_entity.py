
from pydantic import EmailStr
from typing import Optional

from domain.entities.base_entity import BaseEntity

class CustomerEntity(BaseEntity):
    """Customer DTO with Pydantic validation."""
    name: str
    building_name: Optional[str] = None
    address_line_1: Optional[str] = None
    address_line_2: Optional[str] = None
    town: Optional[str] = None
    customer_type_id: int
    price_list_id: int
    email: EmailStr
