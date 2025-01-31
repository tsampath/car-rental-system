from typing import List

from domain.interfaces.i_booking_service import IBookingService
from domain.interfaces.i_booking_repository import IBookingRepository
from domain.entities.booking_entity import BookingEntity

class BookingService(IBookingService):
    """Service layer for Booking operations."""

    def __init__(self, booking_repository: IBookingRepository):
        """Initialize BookingService with BookingRepository."""
        self.booking_repository = booking_repository

    def create_booking(self, booking: BookingEntity) -> BookingEntity:
        """Create a new booking."""
        return self.booking_repository.add(booking)

    def get_all_bookings(self) -> List[BookingEntity]:
        """Retrieve all bookings."""
        return self.booking_repository.get_all()

    def get_booking_by_id(self, booking_id: int) -> BookingEntity:
        """Retrieve a booking by ID."""
        return self.booking_repository.get_by_id(booking_id)

    def update_booking_by_id(self, booking_id: int, booking: BookingEntity) -> BookingEntity:
        """Update a booking by ID."""
        return self.booking_repository.update_by_id(booking_id, booking)

    def delete_booking_by_id(self, booking_id: int) -> bool:
        """Delete a booking by ID."""
        return self.booking_repository.delete_by_id(booking_id)

    def close_booking_by_id(self, booking_id: int) -> bool:
        """Close a booking."""
        return self.booking_repository.close_booking_by_id(booking_id)

    def get_opened_bookings(self) -> List[BookingEntity]:
        """Retrieve all opened bookings."""
        return self.booking_repository.get_opened_bookings()

    def get_opened_booking_by_car(self, car_id: int) -> List[BookingEntity]:
        """Retrieve a booking by ID."""
        return self.booking_repository.get_opened_booking_by_car(car_id)
    
    def get_opened_bookings_by_customer(self, customer_id) -> List[BookingEntity]:
        """Retrieve all opened bookings."""
        return self.booking_repository.get_opened_bookings_by_customer(customer_id)
    
    def get_closed_bookings_by_days(self, number_of_days: int) -> List[BookingEntity]:
        """Retrieve all closed bookings within the last requested days."""
        return self.booking_repository.get_closed_bookings_by_days(number_of_days)
