from tabulate import tabulate

from rental_services.controllers.car_controller import CarController
# import main_entry as main_entry

class CarEntry():
    """Car Entry for car related operations."""

    def __init__(self):
        """Initialize UserService with a UserRepository instance."""
        self.car_controller = CarController()

    def main(self) -> int:
        """Car management functionality."""        

        while True:
            print("\nCar Management")
            print("1. Search Cars")
            print("2. Add Car")
            print("3. Back to Main Menu")
            choice = input("Please select an option (1/2/3): ").strip()

            match choice:
                case "1":
                    return_value = self.search_cars()
                    match return_value:
                        case 6:
                            continue
                        case 7:
                            return
                        case _:
                            pass
                case "2":
                    self.add_car()
                case "3":
                    return
                case _:
                    print("Invalid choice. Please try again.")

    def search_cars(self) -> int:
        while True:
            print("1. Search by Registration Number")
            print("2. Search by Made")
            print("3. Search by Model")
            print("4. Search by Year")
            print("5. View available cars")
            print("6. Back to Previous Menu")
            print("7. Back to Main Menu")
            search_choice = input("Please select an option (1/2/3/4): ").strip()
            match search_choice:
                case "1":
                    registration_number = input("Please enter registration number: ").strip()
                    filtered_cars = self.car_controller.get_car_by_car_id(registration_number)
                    if filtered_cars == None:
                        print("System was unable to find any car as per filter criteria")
                    else:
                        print(tabulate(filtered_cars, headers="keys", tablefmt="fancy_grid"))
                        self.actions_on_selected_car()
                case "2":
                    made = input("Please enter made by: ").strip()
                    filtered_cars = self.car_controller.get_by_make(made)
                    if filtered_cars == None:
                        print("System was unable to find any car per filter criteria")
                    else:
                        print(tabulate(self.convert_car_entities_to_table(filtered_cars), headers="keys", tablefmt="grid"))
                        self.actions_on_selected_car()
                case "3":
                    model = input("Please enter model: ").strip()
                    filtered_cars = self.car_controller.get_car_by_model(model)
                    print(tabulate(self.convert_car_entities_to_table(filtered_cars), headers="keys", tablefmt="grid"))
                case "4":
                    year = input("Please enter year of made: ").strip()
                    filtered_cars = self.car_controller.get_car_by_year(year)
                    print(tabulate(self.convert_car_entities_to_table(filtered_cars), headers="keys", tablefmt="grid"))
                case "5":
                    filtered_cars = self.car_controller.get_car_by_availability(True)
                    print(tabulate(self.convert_car_entities_to_table(filtered_cars), headers="keys", tablefmt="grid"))
                    self.actions_on_selected_car()
                case "6":
                    return 6
                case "7":
                    return 7
                case _:
                    print("Invalid choice. Please try again.")

    
    def add_car(self):
        print("Add a New Car")

        car_id = input("Enter car registration ID: ").strip()
        make = input("Enter car made by: ").strip()
        model = input("Enter car model: ").strip()
        year = self.validate_integer_input("Enter year: ")
        mileage = self.validate_integer_input("Enter mileage: ")
        min_rent_period = self.validate_integer_input("Enter minimum rent period: ")
        max_rent_period = self.validate_integer_input("Enter maximum Rent period: ")

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
            "maximum_rent_period": max_rent_period
        }

        self.car_controller.add_car(car_data)
        print(f"Car added successfully: {car_data}")

    def actions_on_selected_car(self):
        while True:
            print("1. Book Car")
            print("2. Update Car")
            print("3. Delete Car")
            print("4. Back to Previous Menu")

            search_choice = input("Please select an option (1/2/3/4): ").strip()
            match search_choice:
                case "1":
                    registration_number = input("Please enter registration number: ").strip()
                    filtered_car = self.car_controller.get_car_by_car_id(registration_number)
                    print(tabulate(filtered_car, headers="keys", tablefmt="fancy_grid"))
                case "2":
                    registration_number = input("Please enter registration number: ").strip()
                    filtered_car = self.car_controller.get_car_by_car_id(registration_number)
                    if filtered_car == None:
                        print("Car not found!!")
                    else:
                        self.update_car(filtered_car.id, filtered_car.car_id, filtered_car.availability)
                        print("Car was updated successfully")
                        return

                case "3":
                    registration_number = input("Please enter registration number: ").strip()
                    filtered_car = self.car_controller.get_car_by_car_id(registration_number)
                    if filtered_car == None:
                        print("Car not found!!")
                    else: 
                        if self.car_controller.delete_car_by_id(filtered_car.id):
                            print("Car was deleted!!")
                        else:
                            print("Car was not deleted due to some reason!!")

                case "4":
                    return
                case _:
                    print("Invalid choice. Please try again.")

    def update_car(self, id: str, car_Id: str, availability: bool):
        print("Update a Car")
        make = input("Enter car made by: ").strip()
        model = input("Enter car model: ").strip()
        year = self.validate_integer_input("Enter year: ")
        mileage = self.validate_integer_input("Enter mileage: ")
        min_rent_period = self.validate_integer_input("Enter minimum rent period: ")
        max_rent_period = self.validate_integer_input("Enter maximum Rent period: ")

        # Check if all required fields are filled
        if not (make and model):
            print("Error: All fields are required. Please try again.")
            return

        car_data = {
            "id": id,
            "car_id": car_Id,
            "availability": availability,
            "make": make,
            "model": model,
            "year": year,
            "mileage": mileage,
            "minimum_rent_period": min_rent_period,
            "maximum_rent_period": max_rent_period
        }

        if self.car_controller.update_car_by_id(id, car_data) == None:
            print("Car was not updated due to some issue")
        else:
            print("Car was updated successfully")


    def validate_integer_input(self, prompt):
        """Utility function to validate integer input."""
        while True:
            value = input(prompt).strip()
            if value.isdigit():
                return int(value)
            print("Invalid input. Please enter a valid integer.")

    def convert_car_entities_to_table(self, cars):
        """Convert a list of CarEntity objects to a list of dictionaries for tabulation."""
        return [
            {
                "Car ID": car.car_id,
                "Make": car.make,
                "Model": car.model,
                "Year": car.year,
                "Mileage": car.mileage,
                "Min Rent Period": car.minimum_rent_period,
                "Max Rent Period": car.maximum_rent_period,
            }
            for car in cars
        ]

#todo: remove this line when testing done
# CarEntry().main()
