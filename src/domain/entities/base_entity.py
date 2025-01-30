from pydantic import BaseModel
from typing import Optional

class BaseEntity(BaseModel):
    """Base entity for all domain models with an optional id."""
    
    id: Optional[int] = None  # ID is optional for new objects

    class Config:
        orm_mode = True
