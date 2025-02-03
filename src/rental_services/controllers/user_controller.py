from common.enums import CustomerType
from common.enums import PriceList
from domain.services.common_service import CommonService
from domain.entities.user_entity import UserEntity
from domain.services.user_service import UserService
from domain.entities.customer_entity import CustomerEntity
from domain.services.customer_service import CustomerService
from rental_services.service_locator import ServiceLocator
from rental_services.controllers.customer_controller import CustomerController

class UserController:
    """Controller for user registration and related operations."""

    def __init__(self):
        """Initialize CustomerController."""
        self.customer_controller = CustomerController()
    
        self.common_service = CommonService()

        self.user_service: UserService = ServiceLocator.get_user_service()
        self.customer_service: CustomerService = ServiceLocator.get_customer_service()

    def register_user(self, user_data: dict) -> UserEntity:
        """Handles new user registration."""
        
        # Validate email
        if not self.common_service.validate_email(user_data['email']):
            print("Error: Invalid email format. Please enter a valid email.")
            return
        
        # Validate DOB
        if not self.common_service.validate_date(user_data['dob']):
            print("Error: Invalid DOB. Ensure it's in YYYY-MM-DD format and a valid date.")
            return

        # Hash the password
        hashed_password = self.common_service.hash_password(user_data['password'])

        print("\nRegistering new user...")

        # Add new customer
        customer_data = CustomerEntity(
            name = user_data['first_name'] + ' ' + user_data['last_name'],
            # building_name = '',
            # address_line_1 = '',
            # address_line_2 = '',
            # town = '',
            customer_type_id = CustomerType.INDIVIDUAL.value,
            price_list_id = PriceList.Standard.value,
            email = user_data['email'],
        )
        customer  = self.customer_service.add_customer(customer_data)

        # Add user
        new_user = UserEntity(
            first_name = user_data['first_name'],
            last_name = user_data['last_name'],
            dob = user_data['dob'],
            email = user_data['email'],
            password = hashed_password,
            customer_id = customer.id
        )
        self.user_service.add_user(new_user)

        print("Registration successful! You can now log in.")

    def get_all_users(self):
        """Get all registered users."""
        return self.user_service.get_all_users()

    def get_user_by_id(self, user_id: int):
        """Get a user by ID."""
        return self.user_service.get_user_by_id(user_id)

    def delete_user_by_id(self, user_id: int):
        """Delete a user by ID."""
        return self.user_service.delete_user_by_id(user_id)

    def update_user_by_id(self, user_id: int, user_data: dict):
        """Update a user by ID."""
        return self.user_service.update_user_by_id(user_id, UserEntity(**user_data))