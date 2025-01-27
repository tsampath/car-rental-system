# src/domain/entities/base_entity.py

from pydantic import BaseModel
from uuid import UUID
import uuid

class BaseEntity(BaseModel):
    """Base entity for all domain entities."""

    id: UUID = None

    def __init__(self, **kwargs):
        if "id" not in kwargs or kwargs["id"] is None:
            kwargs["id"] = uuid.uuid4()
        super().__init__(**kwargs)

    def to_binary_id(self) -> bytes:
        """Converts the UUID to binary for database storage."""
        return self.id.bytes

    @classmethod
    def from_binary_id(cls, binary_id: bytes):
        """Converts binary ID to UUID."""
        return UUID(bytes=binary_id)
