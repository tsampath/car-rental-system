from .base_repository import BaseRepository
from infrastructure.models.user import User

class UserRepository(BaseRepository):
    """Repository for User model."""
    def __init__(self, session):
        super().__init__(User, session)
