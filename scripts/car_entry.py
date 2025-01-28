from rental_services.controllers.car_controller import CarController
import main_entry as main_entry

def main():
    """Car management functionality."""
    car_controller = CarController()

    while True:
        print("\nCar Management")
        print("1. Search Cars")
        print("2. Add Car")
        print("3. Delete Car")
        print("4. Update Car")
        print("5. Back to Main Menu")
        choice = input("Please select an option (1/2/3/4/5): ").strip()

        if choice == "1":
            print("Searching cars... (functionality not implemented)")

        elif choice == "2":
            print("Add a New Car")

            car_id = input("Enter Car ID: ").strip()
            make = input("Enter Car Make: ").strip()
            model = input("Enter Car Model: ").strip()
            year = validate_integer_input("Enter Year: ")
            mileage = validate_integer_input("Enter Mileage: ")
            min_rent_period = validate_integer_input("Enter Minimum Rent Period: ")
            max_rent_period = validate_integer_input("Enter Maximum Rent Period: ")

            # Check if all required fields are filled
            if not (car_id and make and model):
                print("Error: All fields are required. Please try again.")
                continue

            car_data = {
                "car_id": car_id,
                "make": make,
                "model": model,
                "year": year,
                "mileage": mileage,
                "minimum_rent_period": min_rent_period,
                "maximum_rent_period": max_rent_period
            }

            car_controller.add_car(car_data)

            print(f"Car added successfully: {car_data}")

        elif choice == "3":
            print("Deleting a car... (functionality not implemented)")

        elif choice == "4":
            print("Updating car details... (functionality not implemented)")

        elif choice == "5":
            main_entry.main()
            break

        else:
            print("Invalid choice. Please try again.")

def validate_integer_input(prompt):
    """Utility function to validate integer input."""
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print("Invalid input. Please enter a valid integer.")


#todo: remove this line when testing done
main()
