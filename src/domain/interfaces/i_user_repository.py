from abc import ABC, abstractmethod
from typing import List
from domain.entities.user_entity import UserEntity

class IUserRepository(ABC):
    """Interface for UserRepository."""

    @abstractmethod
    def add(self, user_model) -> UserEntity:
        pass

    @abstractmethod
    def get_all(self) -> List[UserEntity]:
        pass

    @abstractmethod
    def get_by_id(self, user_id: str) -> UserEntity:
        pass

    @abstractmethod
    def delete_by_id(self, user_id: str) -> bool:
        pass

    @abstractmethod
    def update_by_id(self, user_id: str, user_model) -> UserEntity:
        pass
