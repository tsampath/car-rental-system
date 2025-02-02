from datetime import date
from pydantic import EmailStr
from typing import Optional

from domain.entities.base_entity import BaseEntity

class UserEntity(BaseEntity):
    """User DTO with Pydantic validation."""
    first_name: str
    last_name: str
    dob: date
    email: EmailStr
    password: str
    role_id: Optional[int] = None
    customer_id: Optional[int] = None
