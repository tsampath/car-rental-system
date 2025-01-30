from abc import ABC, abstractmethod
from typing import List
from domain.entities.user_entity import UserEntity

class IUserService(ABC):
    """Interface for UserService."""

    @abstractmethod
    def add_user(self, user_entity: UserEntity) -> UserEntity:
        """Add a new user."""
        pass

    @abstractmethod
    def get_all_users(self):
        """Retrieve all users."""
        pass

    @abstractmethod
    def get_user_by_id(self, id: int) -> UserEntity:
        """Retrieve a user by ID."""
        pass

    @abstractmethod
    def delete_user_by_id(self, id: int) -> bool:
        """Delete a user by ID."""
        pass

    @abstractmethod
    def update_user_by_id(self, id: int, user_entity: UserEntity) -> UserEntity:
        """Update a user by ID."""
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> UserEntity:
        """Retrieve a user by email."""
        pass
