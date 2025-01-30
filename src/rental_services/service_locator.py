from infrastructure.db.mysql_db_connection import DB_Connection
from infrastructure.repositories.user_repository import UserRepository
from domain.services.user_service import UserService
from infrastructure.repositories.car_repository import CarRepository
from domain.services.car_service import CarService
from infrastructure.repositories.customer_repository  import CustomerRepository
from domain.services.customer_service  import CustomerService

class ServiceLocator:
    """Resolves dependencies and creates service instances."""

    @staticmethod
    def get_user_service():
        """Resolve and return UserService."""
        db_session = DB_Connection().get_session()
        user_repository = UserRepository(db_session)
        return UserService(user_repository)

    @staticmethod
    def get_car_service():
        """Resolve and return CarService."""
        db_session = DB_Connection().get_session()
        car_repository = CarRepository(db_session)
        return CarService(car_repository)

    @staticmethod
    def get_customer_service():
        """Resolve and return CustomerService."""
        db_session = DB_Connection().get_session()
        car_repository = CustomerRepository(db_session)
        return CustomerService(car_repository)
