# src/infrastructure/repositories/user_repository.py

from infrastructure.models.user_model import UserModel
from domain.entities.user_entity import UserEntity
from domain.interfaces.i_user_repository import IUserRepository
from .base_repository import BaseRepository

class UserRepository(BaseRepository[UserModel, UserEntity], IUserRepository):
    """Repository for UserModel."""

    def __init__(self, session):
        super().__init__(UserModel, session)

    def to_model(self, entity: UserEntity) -> UserModel:
        """Convert UserEntity to UserModel."""
        return UserModel(
            id=entity.to_binary_id(),
            first_name=entity.first_name,
            last_name=entity.last_name,
            dob=entity.dob,
            email=entity.email,
            password=entity.password
        )

    def to_entity(self, model: UserModel) -> UserEntity:
        """Convert UserModel to UserEntity."""
        return UserEntity(
            id=UserEntity.from_binary_id(model.id),
            first_name=model.first_name,
            last_name=model.last_name,
            dob=model.dob,
            email=model.email,
            password=model.password
        )
