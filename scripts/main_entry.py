import getpass

from rental_services.controllers.login_controller import LoginController
from rental_services.controllers.user_controller import UserController
from admin_entry import AdminEntry
from customer_entry import CustomerEntry
from common.enums import Role

def main():
    """Main entry point."""
    user_controller = UserController()
    login_controller = LoginController()
    admin_entry = AdminEntry() 
    customer_entry = CustomerEntry()

    while True:

        print("\nWelcome to Yoobee Car Rental!")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Please select an option (1/2/3): ").strip()

        if choice == "1":
            email = input("Enter Email: ").strip()
            password = getpass.getpass(prompt="Enter your password: ")
            logged_in_user = login_controller.login_user(email, password)
            if logged_in_user != None:
                print("Login successful!")
                if(logged_in_user.role_id == Role.Admin.value):
                    admin_entry.main()
                elif(logged_in_user.role_id == Role.Customer.value):
                    customer_entry.main(logged_in_user.customer_id)
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

            user_controller.register_user(user_data)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()
