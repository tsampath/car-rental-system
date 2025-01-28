from infrastructure.db.mysql_db_connection import DB_Connection
from infrastructure.repositories.user_repository import UserRepository
from domain.services.user_service import UserService

class ServiceLocator:
    """Resolves dependencies and creates service instances."""

    @staticmethod
    def get_user_service():
        """Resolve and return UserService."""
        db_session = DB_Connection().get_session()
        user_repository = UserRepository(db_session)
        return UserService(user_repository)
