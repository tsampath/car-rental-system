from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BaseEntity(BaseModel):
    """Base entity for all domain models with an optional id."""
    
    id: Optional[int] = None  # ID is optional for new objects
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
