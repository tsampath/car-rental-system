from typing import List

from domain.interfaces.i_user_service import IUserService
from domain.interfaces.i_user_repository import IUserRepository
from domain.entities.user_entity import UserEntity

class UserService(IUserService):
    """Service layer for User operations."""

    def __init__(self, user_repository: IUserRepository):
        """Initialize UserService with an IUserRepository implementation."""
        self.user_repository = user_repository

    def add_user(self, user_entity: UserEntity) -> UserEntity:
        """Add a new user."""
        user_model = self.user_repository.add(user_entity)
        return user_entity

    def get_all_users(self) -> List[UserEntity]:
        """Get all users."""
        return self.user_repository.get_all()

    def get_user_by_id(self, user_id: str) -> UserEntity:
        """Get a user by ID."""
        return self.user_repository.get_by_id(user_id)

    def delete_user_by_id(self, user_id: str) -> bool:
        """Delete a user by ID."""
        return self.user_repository.delete_by_id(user_id)

    def update_user_by_id(self, user_id: str, user_entity: UserEntity) -> UserEntity:
        """Update a user by ID."""
        return self.user_repository.update_by_id(user_id, user_entity)
