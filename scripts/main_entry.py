from rental_services.controllers.login_controller import LoginController
from rental_services.controllers.registration_controller import RegistrationController
from car_entry import CarEntry  
import customer_entry as customer_entry

def main():
    """Main entry point."""
    registration_controller = RegistrationController()
    login_controller = LoginController()
    car_entry = CarEntry()

    is_logged_in = False

    while True:
        if not is_logged_in:
            print("\nWelcome to Yoobee Car Rental!")
            print("1. Login")
            print("2. Register")
            print("3. Exit")
            choice = input("Please select an option (1/2/3): ").strip()

            if choice == "1":
                email = input("Enter Email: ").strip()
                password = input("Enter Password: ").strip()
                if login_controller.login_user(email, password):
                    print("Login successful!")
                    is_logged_in = True
                else:
                    print("Login failed. Please try again.")

            elif choice == "2":
                user_data = {
                    "first_name": input("Enter First Name: ").strip(),
                    "last_name": input("Enter Last Name: ").strip(),
                    "dob": input("Enter Date of Birth (YYYY-MM-DD): ").strip(),
                    "email": input("Enter Email: ").strip(),
                    "password": input("Enter Password: ").strip()
                }
                confirm_password = input("Confirm Password: ").strip()
                if confirm_password != user_data["password"]:
                    print("Error: Password confirmation does not match. Please try again.")
                    continue

                registration_controller.register_user(user_data)

            elif choice == "3":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        else:
            print("\nWelcome to Yoobee Car Rental Management System!")
            print("1. Car Management")
            print("2. Customer Management")
            print("3. Logout")
            choice = input("Please select an option (1/2/3): ").strip()

            if choice == "1":
                car_entry.main()

            elif choice == "2":
                customer_entry.main()

            elif choice == "3":
                print("Logged out successfully!")
                is_logged_in = False

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
