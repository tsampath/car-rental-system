from .base_repository import BaseRepository
from infrastructure.models.user_model import UserModel

class UserRepository(BaseRepository):
    """Repository for User model."""
    def __init__(self, session):
        super().__init__(UserModel, session)
