from datetime import date
from pydantic import EmailStr
from domain.entities.base_entity import BaseEntity

class UserEntity(BaseEntity):
    """User DTO with Pydantic validation."""
    first_name: str
    last_name: str
    dob: date
    email: EmailStr
    password: str

    class Config:
        from_attributes = True
