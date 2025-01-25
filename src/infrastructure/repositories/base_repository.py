from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

class BaseRepository:
    """Base repository providing common database operations."""
    def __init__(self, model, session: Session):
        self.model = model
        self.session = session

    def add(self, entity):
        try:
            self.session.add(entity)
            self.session.commit()
            return entity
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def get_all(self):
        return self.session.query(self.model).all()

    def get_by_id(self, entity_id):
        return self.session.query(self.model).get(entity_id)

    def delete_by_id(self, entity_id):
        try:
            entity = self.get_by_id(entity_id)
            if entity:
                self.session.delete(entity)
                self.session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def update_by_id(self, entity_id, **kwargs):
        try:
            entity = self.get_by_id(entity_id)
            if not entity:
                return None
            for key, value in kwargs.items():
                setattr(entity, key, value)
            self.session.commit()
            return entity
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
