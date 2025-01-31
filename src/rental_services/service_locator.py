from infrastructure.db.mysql_db_connection import DB_Connection
from infrastructure.repositories.user_repository import UserRepository
from domain.services.user_service import UserService
from infrastructure.repositories.car_repository import CarRepository
from domain.services.car_service import CarService
from infrastructure.repositories.customer_repository  import CustomerRepository
from domain.services.customer_service  import CustomerService
from infrastructure.repositories.booking_repository import BookingRepository
from domain.services.booking_service  import BookingService

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

    @staticmethod
    def get_booking_service():
        """Resolve and return BookingService."""
        db_session = DB_Connection().get_session()
        booking_repository = BookingRepository(db_session)
        return BookingService(booking_repository)
