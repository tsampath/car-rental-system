from domain.services.common_service import CommonService
from domain.entities.user_entity import UserEntity
from domain.services.user_service import UserService
from rental_services.service_locator import ServiceLocator

class RegistrationController:
    """Controller for user registration and related operations."""

    def __init__(self):
        self.common_service = CommonService()

        """Initialize RegistrationController with UserService."""
        self.user_service: UserService = ServiceLocator.get_user_service()

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
        
        # Add user
        new_user = UserEntity(
            first_name = user_data['first_name'],
            last_name = user_data['last_name'],
            dob = user_data['dob'],
            email = user_data['email'],
            password = hashed_password
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