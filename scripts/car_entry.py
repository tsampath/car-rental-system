from tabulate import tabulate
from typing import List
from datetime import datetime

from rental_services.controllers.car_controller import CarController
from booking_entry import BookingEntry
# import main_entry as main_entry

class CarEntry():
    """Car Entry for car related operations."""

    def __init__(self):
        """Initialize UserService with a UserRepository instance."""
        self.car_controller = CarController()
        self.booking_entry = BookingEntry()

    def main(self) -> int:
        """Car management functionality."""        

        while True:
            print("\nCar Management")
            print("1. Search Available Cars")
            print("2. Search Cars")
            print("3. Add Car")
            print("4. Back to Main Menu")
            choice = input("Please select an option (1/2/3): ").strip()

            match choice:
                case "1":
                    if (self.search_available_cars()):
                        self.actions_on_selected_car()
                    else:
                        print("No cars available for the given date period")
                case "2":
                    return_value = self.search_cars()
                    match return_value:
                        case 6:
                            continue
                        case 7:
                            return
                        case _:
                            pass
                case "3":
                    self.add_car()
                case "4":
                    return
                case _:
                    print("Invalid choice. Please try again.")

    def search_available_cars(self):
        start_date_str = input("Enter booking start date (YYYY-MM-DD): ").strip()
        end_date_str = input("Enter booking end date (YYYY-MM-DD): ").strip()

        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

            if start_date >= end_date:
                print("Error: Start date must be before end date.")
                return
            
            available_cars = self.car_controller.search_available_cars(start_date, end_date)
            if(available_cars != None):
                print(tabulate(self.convert_car_entities_to_table(available_cars), headers="keys", tablefmt="grid"))
                return True
            else:
                return False
        
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    def search_cars(self) -> int:
        while True:
            print("1. Search all cars")
            print("2. Search by Registration Number")
            print("3. Search by Made")
            print("4. Search by Model")
            print("5. Search by Year")
            print("6. Back to Previous Menu")
            print("7. Back to Main Menu")
            search_choice = input("Please select an option (1/2/3/4/5/6/7): ").strip()
            match search_choice:
                case "1":
                    filtered_cars = self.car_controller.get_all_cars()
                    print(tabulate(self.convert_car_entities_to_table(filtered_cars), headers="keys", tablefmt="grid"))
                    self.actions_on_selected_car()                            
                case "2":
                    registration_number = input("Please enter registration number: ").strip()
                    filtered_cars = self.car_controller.get_car_by_car_id(registration_number)
                    if filtered_cars == None:
                        print("System was unable to find any car as per filter criteria")
                    else:
                        print(tabulate(filtered_cars, headers="keys", tablefmt="fancy_grid"))
                        self.actions_on_selected_car()
                case "3":
                    made = input("Please enter made by: ").strip()
                    filtered_cars = self.car_controller.get_by_make(made)
                    if filtered_cars == None:
                        print("System was unable to find any car per filter criteria")
                    else:
                        print(tabulate(self.convert_car_entities_to_table(filtered_cars), headers="keys", tablefmt="grid"))
                        self.actions_on_selected_car()
                case "4":
                    model = input("Please enter model: ").strip()
                    filtered_cars = self.car_controller.get_car_by_model(model)
                    if filtered_cars == None:
                        print("System was unable to find any car per filter criteria")
                    else:
                        print(tabulate(self.convert_car_entities_to_table(filtered_cars), headers="keys", tablefmt="grid"))
                        self.actions_on_selected_car()
                case "5":
                    year = input("Please enter year of made: ").strip()
                    filtered_cars = self.car_controller.get_car_by_year(year)
                    if filtered_cars == None:
                        print("System was unable to find any car per filter criteria")
                    else:
                        print(tabulate(self.convert_car_entities_to_table(filtered_cars), headers="keys", tablefmt="grid"))
                        self.actions_on_selected_car()
                case "6":
                    return int(search_choice)
                case "7":
                    return int(search_choice)
                case _:
                    print("Invalid choice. Please try again.")

    
    def add_car(self):
        print("Add a New Car")

        car_id = input("Enter car registration ID: ").strip()
        make = input("Enter car made by: ").strip()
        model = input("Enter car model: ").strip()
        year = self.validate_integer_input("Enter year: ")
        mileage = self.validate_integer_input("Enter mileage: ")
        min_rent_period = self.validate_integer_input("Enter minimum rent period (Days): ")
        max_rent_period = self.validate_integer_input("Enter maximum Rent period (Days):")
        rate_per_day = self.validate_float("Enter rate per day($):")
        

        # Check if all required fields are filled
        if not (car_id and make and model):
            print("Error: All fields are required. Please try again.")
            return

        car_data = {
            "car_id": car_id,
            "make": make,
            "model": model,
            "year": year,
            "mileage": mileage,
            "minimum_rent_period": min_rent_period,
            "maximum_rent_period": max_rent_period,
            "rate_per_day": rate_per_day
        }

        self.car_controller.add_car(car_data)
        print(f"Car added successfully: {car_data}")

    def actions_on_selected_car(self) -> int:
        while True:
            print("1. Book Car")
            print("2. Update Car")
            print("3. Delete Car")
            print("4. Back to Previous Menu")

            search_choice = input("Please select an option (1/2/3/4): ").strip()
            match search_choice:
                case "1":
                    self.booking_entry.add_booking()
                case "2":
                    filtered_car = self.get_car()
                    if filtered_car != None:
                        self.update_car(filtered_car)
                        print("Car was updated successfully")

                case "3":
                    filtered_car = self.get_car()
                    if filtered_car != None: 
                        if self.car_controller.delete_car_by_id(filtered_car.id):
                            print("Car was deleted!!")
                        else:
                            print("Car was not deleted due to some reason!!")

                case "4":
                    return int(search_choice)
                case _:
                    print("Invalid choice. Please try again.")

    def get_car(self) -> any: 
        registration_number = input("Please enter registration number of a car: ").strip()
        filtered_car = self.car_controller.get_car_by_car_id(registration_number)
        if filtered_car == None:
            print("System was unable to find any car by given registration number")
            return None
        else:
            return filtered_car
        
    def update_car(self, car_data):
        print("Update a Car")
        car_data.mileage = self.validate_integer_input("Enter mileage: ")
        car_data.minimum_rent_period = self.validate_integer_input("Enter minimum rent period: ")
        car_data.maximum_rent_period = self.validate_integer_input("Enter maximum Rent period: ")

        if self.car_controller.update_car_by_id(car_data.id, car_data) == None:
            print("Car was not updated due to some issue")
        else:
            print("Car was updated successfully")



    def validate_integer_input(self, prompt):
        while True:
            value = input(prompt).strip()
            if value.isdigit():
                return int(value)
            print("Invalid input. Please enter a valid integer.")

    def convert_car_entities_to_table(self, cars):
        """Convert a list of CarEntity objects to a list of dictionaries for tabulation."""
        return [
            {
                "Car Registration ID": car.car_id,
                "Make": car.make,
                "Model": car.model,
                "Year": car.year,
                "Mileage": car.mileage,
                "Min Rent Period": car.minimum_rent_period,
                "Max Rent Period": car.maximum_rent_period,
            }
            for car in cars
        ]
    
    def validate_float(self, prompt) -> float:
        """Prompt user for a float and keep retrying until valid."""
        while True:
            user_input = input(prompt)
            try:
                value = float(user_input)
                return value  # success
            except ValueError:
                print(f"Error: '{user_input}' is not a valid floating-point number. Please try again.")

#todo: remove this line when testing done
# CarEntry().main()
