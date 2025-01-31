from abc import ABC, abstractmethod
from typing import List
from domain.entities.booking_entity import BookingEntity

class IBookingService(ABC):
    """Interface for BookingService."""

    @abstractmethod
    def create_booking(self, booking: BookingEntity) -> BookingEntity:
        pass

    @abstractmethod
    def get_all_bookings(self) -> List[BookingEntity]:
        pass

    @abstractmethod
    def get_booking_by_id(self, booking_id: int) -> BookingEntity:
        pass

    @abstractmethod
    def update_booking_by_id(self, booking_id: int, booking: BookingEntity) -> BookingEntity:
        pass

    @abstractmethod
    def delete_booking_by_id(self, booking_id: int) -> bool:
        pass

    @abstractmethod
    def close_booking_by_id(self, booking_id: int) -> bool:
        pass

    def get_opened_bookings(self) -> List[BookingEntity]:
        """Retrieve all opened bookings."""
        pass

    @abstractmethod
    def get_opened_booking_by_car(self, car_id: int) -> BookingEntity:
        """Retrieve a open booking by car ID."""
        pass

    @abstractmethod
    def get_opened_bookings_by_customer(self, customer_id: int) -> List[BookingEntity]:
        """Retrieve open bookings by open ."""
        pass

    @abstractmethod
    def get_closed_bookings_by_days(self, number_of_days: int) -> List[BookingEntity]:
        """Retrieve all closed bookings within the last requested days."""
        pass