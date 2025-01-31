from datetime import date
from pydantic import EmailStr
from typing import Optional
from datetime import datetime

from domain.entities.base_entity import BaseEntity

class UserEntity(BaseEntity):
    """User DTO with Pydantic validation."""
    first_name: str
    last_name: str
    dob: date
    email: EmailStr
    password: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
