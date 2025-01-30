from abc import ABC, abstractmethod
from typing import List
from domain.entities.user_entity import UserEntity

class IUserRepository(ABC):
    """Interface for UserRepository."""

    @abstractmethod
    def add(self, user_model: UserEntity) -> UserEntity:
        """Add a new user."""
        pass

    @abstractmethod
    def get_all(self) -> List[UserEntity]:
        """Retrieve all users."""
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> UserEntity:
        """Retrieve a user by ID."""
        pass

    @abstractmethod
    def delete_by_id(self, user_id: int) -> bool:
        """Delete a user by ID."""
        pass

    @abstractmethod
    def update_by_id(self, user_id: int, user_model: UserEntity) -> UserEntity:
        """Update a user by ID."""
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> UserEntity:
        """Retrieve a user by email."""
        pass

    @abstractmethod
    def to_model(self, entity: UserEntity):
        """Convert a UserEntity to a UserModel."""
        pass

    @abstractmethod
    def to_entity(self, model) -> UserEntity:
        """Convert a UserModel to a UserEntity."""
        pass
