from domain.service.common_service import CommonService
from domain.entities.user_entity import UserEntity
from infrastructure.services.user_service import UserService
from infrastructure.db.mysql_db_connection import DB_Connection

class RegistrationController:
    """Handles user registration."""

    def __init__(self):
        self.common_service = CommonService()
        # Get session and UserService        
        self.session = DB_Connection().get_session()
        self.user_service = UserService(self.session)

    def register_user(self, user_data: dict) -> UserEntity:
        """Handles new user registration."""
        
        # Validate email
        if not self.common_service.validate_email(user_data['username']):
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
            email = user_data['username'],
            password = hashed_password
        )
        self.user_service.add_user(new_user)

        print("Registration successful! You can now log in.")

    def get_all_users(self):
        """Get all registered users."""
        return self.user_service.get_all_users()

    def get_user_by_id(self, user_id: str):
        """Get a user by ID."""
        return self.user_service.get_user_by_id(user_id)

    def delete_user_by_id(self, user_id: str):
        """Delete a user by ID."""
        return self.user_service.delete_user_by_id(user_id)

    def update_user_by_id(self, user_id: str, user_data: dict):
        """Update a user by ID."""
        return self.user_service.update_user_by_id(user_id, UserEntity(**user_data))