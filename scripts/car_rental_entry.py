# scripts/car_rental_entry.py

from rental_services.controllers.registration_controller import RegistrationController
from rental_services.controllers.login_controller import LoginController

def main():
    """Main entry point."""
    registration_controller = RegistrationController()
    login_controller = LoginController()

    while True:
        print("\nWelcome to Yoobee Car Rental!")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Please select an option (1/2/3): ").strip()

        if choice == "1":
            # Login
            email = input("Enter Email: ").strip()
            password = input("Enter Password: ").strip()
            login_controller.login_user(email, password)

        elif choice == "2":
            # Register
            user_data = {
                "first_name": input("Enter First Name: ").strip(),
                "last_name": input("Enter Last Name: ").strip(),
                "dob": input("Enter Date of Birth (YYYY-MM-DD): ").strip(),
                "email": input("Enter Email: ").strip(),
                "password": input("Enter Password: ").strip()
            }

            # Confirm password
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

if __name__ == "__main__":
    main()
