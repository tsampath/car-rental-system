from typing import Generic, TypeVar, List
from sqlalchemy.orm import Session

TModel = TypeVar("TModel")  # Type for database models
TEntity = TypeVar("TEntity")  # Type for domain entities

class BaseRepository(Generic[TModel, TEntity]):
    """Base repository providing generic database operations."""

    def __init__(self, model: TModel, session: Session):
        self.model = model
        self.session = session

    def add(self, entity: TEntity) -> TEntity:
        """Convert entity to model, save it to the database, and return the entity."""
        model_instance = self.to_model(entity)
        self.session.add(model_instance)
        self.session.commit()
        return self.to_entity(model_instance)

    def get_all(self) -> List[TEntity]:
        """Retrieve all records and convert them to entities."""
        records = self.session.query(self.model).all()
        return [self.to_entity(record) for record in records]

    def get_by_id(self, entity_id: str) -> TEntity:
        """Retrieve a record by ID and convert it to an entity."""
        record = self.session.query(self.model).get(entity_id)
        return self.to_entity(record) if record else None

    def delete_by_id(self, entity_id: str) -> bool:
        """Delete a record by ID."""
        record = self.session.query(self.model).get(entity_id)
        if record:
            self.session.delete(record)
            self.session.commit()
            return True
        return False

    def update_by_id(self, entity_id: str, entity: TEntity) -> TEntity:
        """Update a record by ID with new data and return the updated entity."""
        record = self.session.query(self.model).get(entity_id)
        if record:
            for key, value in entity.dict(exclude={"id"}).items():
                setattr(record, key, value)
            self.session.commit()
            return self.to_entity(record)
        return None

    def to_model(self, entity: TEntity) -> TModel:
        """Convert a domain entity to a database model."""
        raise NotImplementedError("Subclasses must implement to_model method.")

    def to_entity(self, model: TModel) -> TEntity:
        """Convert a database model to a domain entity."""
        raise NotImplementedError("Subclasses must implement to_entity method.")
