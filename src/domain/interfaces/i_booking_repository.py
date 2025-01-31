from abc import ABC, abstractmethod
from typing import List

from domain.entities.booking_entity import BookingEntity

class IBookingRepository(ABC):
    """Interface for BookingRepository."""

    @abstractmethod
    def add(self, booking: BookingEntity) -> BookingEntity:
        """Add a new booking."""
        pass

    @abstractmethod
    def get_all(self) -> List[BookingEntity]: 
        """Retrieve all bookings."""
        pass

    @abstractmethod
    def get_opened_bookings(self) -> List[BookingEntity]:
        """Retrieve all opened bookings."""
        pass

    @abstractmethod
    def get_by_id(self, booking_id: int) -> BookingEntity:
        """Retrieve a booking by ID."""
        pass

    @abstractmethod
    def update_by_id(self, booking_id: int, booking: BookingEntity) -> BookingEntity:
        """Update an existing booking."""
        pass

    @abstractmethod
    def delete_by_id(self, booking_id: int) -> bool:
        """Delete a booking by ID."""
        pass

    @abstractmethod
    def close_booking_by_id(self, booking_id: int) -> bool:
        """Mark a booking as closed."""
        pass

    @abstractmethod
    def get_opened_booking_by_car(self, car_id: int) -> List[BookingEntity]:
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