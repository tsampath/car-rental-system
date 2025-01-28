from abc import ABC, abstractmethod
from typing import List
from domain.entities.user_entity import UserEntity

class IUserService(ABC):
    """Interface for UserService."""

    @abstractmethod
    def add_user(self, user_entity: UserEntity) -> UserEntity:
        pass

    @abstractmethod
    def get_all_users(self) -> List[UserEntity]:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: str) -> UserEntity:
        pass

    @abstractmethod
    def delete_user_by_id(self, user_id: str) -> bool:
        pass

    @abstractmethod
    def update_user_by_id(self, user_id: str, user_entity: UserEntity) -> UserEntity:
        pass
