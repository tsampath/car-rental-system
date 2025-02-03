from typing import List

from domain.services.common_service import CommonService
from domain.entities.booking_entity import BookingEntity
from domain.services.booking_service import BookingService
from rental_services.service_locator import ServiceLocator

class BookingController:
    """Controller for booking related operations."""

    def __init__(self):
        self.common_service = CommonService()

        """Initialize Booking Controller with BookingService."""
        self.booking_service: BookingService = ServiceLocator.get_booking_service()
        
        # Add booking
    def add_booking(self, booking_data: dict) -> BookingEntity:        

        # Validate Start Date
        if not self.common_service.validate_date(booking_data['booking_start_date']):
            print("Error: Invalid Start Date. Ensure it's in YYYY-MM-DD format and a valid date.")
            return

        # Validate Start Date
        if not self.common_service.validate_date(booking_data['booking_end_date']):
            print("Error: Invalid End Date . Ensure it's in YYYY-MM-DD format and a valid date.")
            return

        new_booking = BookingEntity(
            car_id = booking_data['car_id'],
            customer_id = booking_data['customer_id'],
            booking_start_date = booking_data['booking_start_date'],
            booking_end_date = booking_data['booking_end_date'],
            is_closed = False,
            status_id = booking_data['status_id'],
        )
        self.booking_service.create_booking(new_booking)

    def get_all_bookings(self):
        """Get all registered bookings."""
        return self.booking_service.get_all_bookings()

    def get_booking_by_id(self, id: int):
        """Get a booking by ID."""
        return self.booking_service.get_booking_by_id(id)

    def delete_booking_by_id(self, id: int):
        """Delete a booking by ID."""
        return self.booking_service.delete_booking_by_id(id)

    def update_booking_by_id(self, id: int, booking_data: dict):
        """Update a booking by ID."""
        return self.booking_service.update_booking_by_id(id, booking_data)
   
    def close_booking_by_id(self, id: int):
        """Close a booking by ID."""
        return self.booking_service.close_booking_by_id(id)

    def get_opened_bookings(self):
        """Get opened bookings."""
        return self.booking_service.get_opened_bookings()

    def get_opened_booking_by_car(self, car_id):
        """Get opened booking by car"""
        return self.booking_service.get_opened_booking_by_car(car_id)

    def get_opened_booking_by_customer(self, customer_id):
        """Get opened booking by car"""
        return self.booking_service.get_opened_bookings_by_customer(customer_id)
    
    def get_closed_bookings_by_days(self, number_of_days: int) -> List[BookingEntity]:
        """Retrieve all closed bookings within the last requested days."""
        return self.booking_service.get_closed_bookings_by_days(number_of_days)
