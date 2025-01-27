from typing import List
from infrastructure.repositories.user_repository import UserRepository
from domain.entities.user_entity import UserEntity
from infrastructure.models.user_model import UserModel

class UserService:
    """Service layer for User operations."""

    def __init__(self, db_session):
        """Initialize UserService and create UserRepository."""
        self.user_repository = UserRepository(db_session)

    def add_user(self, user_entity: UserEntity) -> UserEntity:
        """Add a new user."""
        user_model = UserModel(
            id=user_entity.to_binary_id(),
            **user_entity.dict(exclude={"id"})  # Exclude 'id' from the DTO dictionary
        )
        user = self.user_repository.add(user_model)
        return UserEntity(
            id=UserEntity.from_binary_id(user.id),
            **{k: v for k, v in user.__dict__.items() if k != "id"}  # Exclude 'id' here as well
        )

    def get_all_users(self) -> List[UserEntity]:
        """Get all users."""
        users = self.user_repository.get_all()
        return [
            UserEntity(
                id=UserEntity.from_binary_id(user.id),
                **{k: v for k, v in user.__dict__.items() if k != "id"}  # Exclude 'id' here as well
            )
            for user in users
        ]

    def get_user_by_id(self, user_id: str) -> UserEntity:
        """Get a user by ID."""
        user = self.user_repository.get_by_id(user_id)
        if user:
            return UserEntity(
                id=UserEntity.from_binary_id(user.id),
                **{k: v for k, v in user.__dict__.items() if k != "id"}  # Exclude 'id' here as well
            )
        return None

    def delete_user_by_id(self, user_id: str) -> bool:
        """Delete a user by ID."""
        return self.user_repository.delete_by_id(user_id)

    def update_user_by_id(self, user_id: str, user_entity: UserEntity) -> UserEntity:
        """Update a user by ID."""
        updated_user = self.user_repository.update_by_id(
            user_id, **user_entity.dict(exclude={"id"})
        )
        if updated_user:
            return UserEntity(
                id=UserEntity.from_binary_id(updated_user.id),
                **{k: v for k, v in updated_user.__dict__.items() if k != "id"}  # Exclude 'id' here as well
            )
        return None
