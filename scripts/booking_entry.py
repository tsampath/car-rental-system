from tabulate import tabulate
from typing import List
from datetime import datetime

from common.enums import BookingStatus
from rental_services.controllers.booking_controller import BookingController
from rental_services.controllers.car_controller import CarController
from rental_services.controllers.customer_controller import CustomerController
from domain.entities.booking_entity import BookingEntity
from domain.entities.car_entity import CarEntity
from common.constants import Constants

class BookingEntry():
    """Booking Entry for booking related operations."""

    def __init__(self):
        """Initialize BookingController instance."""
        self.booking_controller = BookingController()
        """Initialize CarController instance."""
        self.car_controller = CarController()
        """Initialize CustomerController instance."""
        self.customer_controller = CustomerController()

    def main(self) -> int:
        """Booking management functionality."""        

        while True:
            print("\nBooking Management")
            print("1. Search Bookings")
            print("2. Add Booking")
            print("3. Back to Main Menu")
            choice = input("Please select an option (1/2/3): ").strip()

            match choice:
                case "1":
                    return_value = self.search_bookings()
                    match return_value:
                        case 5:
                            continue
                        case 6:
                            return
                        case _:
                            pass
                case "2":
                    self.add_booking(BookingStatus.Approved.value, -1)
                case "3":
                    return
                case _:
                    print("Invalid choice. Please try again.")

    def search_bookings(self) -> int:
        while True:
            print("1. Search all open bookings")
            print("2. Search closed bookings for last 30 days")
            print("3. View open booking by car")
            print("4. View open bookings by customer")
            print("5. Back to Previous Menu")
            print("6. Back to Main Menu")
            search_choice = input("Please select an option (1/2/3/4/5/6): ").strip()
            match search_choice:
                case "1":
                    filtered_bookings = self.booking_controller.get_opened_bookings()
                    print(tabulate(self.convert_booking_entities_to_table(filtered_bookings), headers="keys", tablefmt="grid"))
                    self.actions_on_selected_booking()
                case "2":
                    filtered_bookings = self.booking_controller.get_closed_bookings_by_days(30)
                    print(tabulate(self.convert_booking_entities_to_table(filtered_bookings), headers="keys", tablefmt="grid"))
                    self.actions_on_selected_booking()
                case "3":
                    filtered_car = self.get_car()
                    if filtered_car != None:
                        filtered_bookings = self.booking_controller.get_opened_booking_by_car(filtered_car.id)
                        if filtered_bookings == None:
                            print("System was unable to find any booking by given registration number ")
                        else:
                            print(tabulate(self.convert_booking_entities_to_table(filtered_bookings), headers="keys", tablefmt="grid"))
                            self.actions_on_selected_booking()
                case "4":
                    name = input("Please enter customer name: ").strip()
                    filtered_customers = self.customer_controller.get_customer_by_name(name)
                    if filtered_customers == None:
                        print("System was unable to find any customer as per filter criteria")
                    else:
                        print("Customer Record:")
                        print(tabulate(self.convert_customer_entities_to_table(filtered_customers), headers="keys", tablefmt="grid"))
                        customer_id = input("Please enter customer id: ").strip()
                        filtered_customer = self.customer_controller.get_customer_by_id(customer_id)
                        if filtered_customer == None:
                            print("System was unable to find any customer by given customer id")
                        else:
                            filtered_bookings = self.booking_controller.get_opened_booking_by_customer(filtered_customer.id)
                            if filtered_bookings == None:
                                print("System was unable to find any booking by given customer id")
                            else:
                                print(tabulate(self.convert_booking_entities_to_table(filtered_bookings), headers="keys", tablefmt="grid"))
                                self.actions_on_selected_booking()             
                case "5":
                    return int(search_choice)
                case "6":
                    return int(search_choice)
                case _:
                    print("Invalid choice. Please try again.")

    
    def add_booking(self, status_id: int, customer_id: int):
        print("Add a New Booking")
        filtered_car = self.get_car()
        if filtered_car != None:
            if(customer_id == -1):
                customer_id_str = input("Please enter customer id: ").strip()
                filtered_customer = self.customer_controller.get_customer_by_id(customer_id_str)
                if filtered_customer == None:
                    print("System was unable to find any customer by given customer id")
                else:
                    customer_id = filtered_customer.id
            
            while True:
                booking_start_date = input("Booking start date (YYYY-MM-DD): ").strip()
                if self.validate_date(booking_start_date):
                    booking_end_date = input("Booking end date (YYYY-MM-DD): ").strip()
                    if self.validate_date(booking_end_date):
                        additional_comment = input("Additional comment : ").strip()
                        start_date = datetime.strptime(booking_start_date, "%Y-%m-%d")
                        end_date = datetime.strptime(booking_end_date, "%Y-%m-%d")
                        if start_date >= end_date:
                            print("Error: Start date must be before end date.")
                            return
                        if(self.car_controller.is_car_available(filtered_car.id, start_date, end_date)):

                            num_days = (end_date - start_date).days
                            total_booking_cost = (num_days * filtered_car.rate_per_day)
                            gst = (total_booking_cost * Constants.GST_RATE)/100
                            total_cost = round(total_booking_cost + gst, 2)
                            print(f"Total cost as per start and end date ${total_cost}")
                            confirmation = input("Please hit enter button to proceed. If you would like to see different option please type exit and hit enter: ")
                            if(confirmation == 'exit'):
                                return
                            booking_data = {
                                "car_id": int(filtered_car.id),
                                "customer_id": customer_id,
                                "booking_start_date": booking_start_date,
                                "booking_end_date": booking_end_date,
                                "additional_comment": additional_comment,
                                "status_id": status_id,
                                "total_cost": total_cost
                            }
                            self.booking_controller.add_booking(booking_data)
                            print("Booking added successfully!!")
                        else:
                            print("Selected car is not available within given date period")
                        return
                    else:
                        print("Invalid date please try again")
                        continue
                else:
                    print("Invalid date please try again")
                    continue

    def actions_on_selected_booking(self):
        while True:
            print("1. Update Booking")
            print("2. Delete Booking")
            print("3. Close Booking")
            print("4. Back to Previous Menu")

            search_choice = input("Please select an option (1/2/3/4): ").strip()
            match search_choice:
                case "1":
                    booking = self.get_booking()
                    if(booking):
                        self.update_booking(booking)
                case "2":
                    booking = self.get_booking()
                    if(booking):
                        if self.booking_controller.delete_booking_by_id(booking.id):
                            print("Booking was deleted!!")
                        else:
                            print("Booking was not deleted due to some reason!!")                
                case "3":
                    booking = self.get_booking()
                    if(booking):
                        if self.booking_controller.close_booking_by_id(booking.id):
                            print("Booking was successfully closed!!")
                        else:
                            print("Booking was not closed due to some reason!!")             
                case "4":
                    return
                case _:
                    print("Invalid choice. Please try again.")

    def get_booking(self) -> BookingEntity: 
        booking_id = input("Please enter booking id: ").strip()
        filtered_booking = self.booking_controller.get_booking_by_id(booking_id)
        if filtered_booking == None:
            print("Booking not found!!")
            return None
        else:
            return filtered_booking

    def get_car(self) -> CarEntity: 
        registration_number = input("Please enter registration number of a car: ").strip()
        filtered_car = self.car_controller.get_car_by_car_id(registration_number)
        if filtered_car == None:
            print("System was unable to find any car by given registration number")
            return None
        else:
            return filtered_car

    def update_booking(self, booking: any) -> int:
        if(booking.is_closed):
            additional_comment = input("Additional comment : ").strip()
            booking.additional_comment = booking.additional_comment + "\n" + additional_comment
            self.booking_controller.update_booking_by_id(booking.id, booking)
            print(f"Booking updated successfully: {booking}")
        else:
            booking_start_date = input("Booking start date (YYYY-MM-DD): ").strip()
            if self.validate_date(booking_start_date):
                booking_end_date = input("Booking end date (YYYY-MM-DD): ").strip()
                if self.validate_date(booking_start_date):
                    additional_comment = input("Additional comment : ").strip()
                    booking.booking_start_date = booking_start_date
                    booking.booking_end_date = booking_end_date
                    booking.additional_comment = booking.additional_comment + additional_comment if booking.additional_comment != None else  additional_comment

                    self.booking_controller.update_booking_by_id(booking.id, booking)
                    print(f"Booking updated successfully: {booking}")
                    return 1
                else:
                    print("Invalid date please try again")
                    return -1
            else:
                print("Invalid date please try again")
                return -1

    def validate_integer_input(self, prompt):
        """Utility function to validate integer input."""
        while True:
            value = input(prompt).strip()
            if value.isdigit():
                return int(value)
            print("Invalid input. Please enter a valid integer.")

    def convert_booking_entities_to_table(self, bookings: List[BookingEntity]):
        """Convert a list of BookingEntity objects to a list of dictionaries for tabulation."""
        return [
            {
                "Booking ID": booking.id,
                "Car Id": booking.car_id,
                "Customer Id": booking.customer_id,
                "Booking Start Date": booking.booking_start_date,
                "Booking End Date": booking.booking_end_date,
                "Closed": booking.is_closed,
                "Closed Date": booking.closed_date,
                "Total Cost": booking.total_cost,
                "Status": 'Pending' if BookingStatus.Pending.value == booking.status_id else 'Approved',
                "Additional Comment": booking.additional_comment
            }
            for booking in bookings
        ]
    
    def convert_customer_entities_to_table(self, customers):
        """Convert a list of CustomerEntity objects to a list of dictionaries for tabulation."""
        return [
            {
                "Id": customer.id,
                "Name": customer.name,
                "Unit/Level/Floor": customer.building_name,
                "Street Number and Name": customer.address_line_1,
                "Town": customer.town,
                "Customer Type": 'Individual' if customer.customer_type_id == 1 else 'Corporate',
                "Price List": 'Standard' if customer.price_list_id == 1 else 'Loyal'
            }
            for customer in customers
        ]

    def validate_date(self, date: str) -> bool:
        """Validates a date format (YYYY-MM-DD) and checks if it's a real date."""
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            return False
#todo: remove this line when testing done
# BookingEntry().main()
