from rental_services.controllers.booking_controller import BookingController
from rental_services.controllers.car_controller import CarController
from rental_services.controllers.customer_controller import CustomerController
from booking_entry import BookingEntry
from car_entry import CarEntry
from manage_customer_entry import ManageCustomerEntry

class AdminEntry():
    """Admin Entry for admin related operations."""

    def __init__(self):
        """Initialize BookingEntry instance."""
        self.booking_entry = BookingEntry()
        """Initialize CarEntry instance."""
        self.car_entry = CarEntry()
        """Initialize CustomerEntry instance."""
        self.manage_customer_entry = ManageCustomerEntry()


    def main(self) -> int:
    
        while True:
            """Booking management functionality."""                             
            print("\nWelcome to Yoobee Car Rental Management System!")
            print("1. Booking Management")
            print("2. Car Management")
            print("3. Customer Management")
            print("4. Logout")
            choice = input("Please select an option (1/2/3): ").strip()
            match choice:
                case "1":
                    self.booking_entry.main()
                case "2":
                    self.car_entry.main()
                case "3":
                    self.manage_customer_entry.main()
                case "4":
                    print("Logged out successfully!")
                    return

                case _:
                    print("Invalid choice. Please try again.")
