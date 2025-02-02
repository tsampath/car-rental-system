from booking_entry import BookingEntry
from car_entry import CarEntry
from car_entry import CarEntry
from common.enums import BookingStatus

class CustomerEntry():
    """Customer Entry for customer related operations."""

    def __init__(self):
        """Initialize BookingEntry instance."""
        self.booking_entry = BookingEntry()
        self.car_entry = CarEntry()

        """Initialize CarEntry instance."""
        self.car_entry = CarEntry()

    def main(self, customer_id: int) -> int:
        
        while True:
            print("\nBooking Management")
            print("1. Search Available Cars")
            print("2. Request Booking")
            print("3. Logout")

            choice = input("Please select an option (1/2/3): ").strip()

            match choice:
                case "1":
                    if (not self.car_entry.search_available_cars()):
                        print("No cars available for the given date period")
                case "2":
                    self.booking_entry.add_booking(BookingStatus.Pending, customer_id)
                case "3":
                    return
                case _:
                    print("Invalid choice. Please try again.")
    
