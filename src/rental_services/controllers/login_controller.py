from rental_services.service_locator import ServiceLocator
from domain.services.common_service import CommonService

class LoginController:
    """Controller for user login."""

    def __init__(self):
        """Initialize LoginController with UserService."""
        self.user_service = ServiceLocator.get_user_service()
        self.common_service = CommonService()

    def login_user(self, email: str, password: str) -> bool:
        """Authenticate the user with the given email and password."""
        if not self.common_service.validate_email(email):
            print("Error: Invalid email format.")
            return False

        user = self.user_service.get_user_by_email(email)
        if not user:
            print("Error: User not found.")
            return False

        hashed_password = self.common_service.hash_password(password)
        if user.password != hashed_password:
            print("Error: Incorrect password.")
            return False

        print(f"Welcome back, {user.first_name}!")
        return True
