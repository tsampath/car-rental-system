from domain.service.common_service import CommonService
from infrastructure.models.user  import User
from infrastructure.repositories.user_repository import UserRepository
from infrastructure.db.mysql_db_connection import DB_Connection

class RegistrationController:
    """Handles user registration."""

    def __init__(self):
        self.common_service = CommonService()
        # Get session and repository
        self.session = DB_Connection().get_session()
        self.user_repo = UserRepository(self.session)

    def register(self, first_name, last_name, dob, username, password):
        """Handles new user registration."""
        
        # Check for empty fields
        if not all([first_name, last_name, dob, username, password]):
            print("Error: All fields are required.")
            return

        # Validate email
        if not self.common_service.validate_email(username):
            print("Error: Invalid email format. Please enter a valid email.")
            return
        
        # Validate DOB
        if not self.common_service.validate_date(dob):
            print("Error: Invalid DOB. Ensure it's in YYYY-MM-DD format and a valid date.")
            return

        # Hash the password
        hashed_password = self.common_service.hash_password(password)

        print("\nRegistering new user...")
        
        # Add user
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            email=username,
            password=hashed_password
        )
        self.user_repo.add(new_user)

        print("Registration successful! You can now log in.")
