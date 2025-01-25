from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy import Column, BINARY
from sqlalchemy.ext.hybrid import hybrid_property
import uuid

@as_declarative()
class BaseModel:
    """Base model for all SQLAlchemy models, includes id and UUID translation."""
    id = Column(BINARY(16), primary_key=True, unique=True, nullable=False, default=lambda: uuid.uuid4().bytes)

    @hybrid_property
    def uuid(self):
        """Returns the UUID as a string from the BINARY(16) id."""
        return str(uuid.UUID(bytes=self.id))
