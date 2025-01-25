from rental_services.startup import Startup
from rental_services.login_controller import LoginController
from rental_services.registration_controller import RegistrationController

def main():
    """Main function to handle user choice and input."""
    #Run rental services startup  
    startup = Startup()
    login_controller = LoginController()
    registration_controller = RegistrationController()

    while True:
        print("\nWelcome to Yoobee Car Rental!")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        
        choice = input("Please select an option (1/2/3): ").strip()

        if choice == "1":
            username = input("Enter username (email): ").strip()
            password = input("Enter password: ").strip()
            login_controller.login(username, password)  

        elif choice == "2":
            print("\nUser Registration:")
            first_name = input("Enter First Name: ").strip()
            last_name = input("Enter Last Name: ").strip()
            dob = input("Enter Date of Birth (YYYY-MM-DD): ").strip()
            username = input("Enter Username (Email): ").strip()
            
            # Ensure password confirmation
            while True:
                password = input("Enter Password: ").strip()
                confirm_password = input("Confirm Password: ").strip()
                if password == confirm_password:
                    break
                print("Error: Passwords do not match. Please try again.")

            registration_controller.register(first_name, last_name, dob, username, password)  # Call register

        elif choice == "3":
            print("Thank you for using Yoobee Car Rental! Goodbye.")
            break  # Exit loop
        
        else:
            print("Invalid selection. Please choose again.")

if __name__ == "__main__":
    main()
