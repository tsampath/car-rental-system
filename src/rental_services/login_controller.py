from domain.service.common_service import CommonService

class LoginController:
    """Handles user login."""

    def __init__(self):
        self.common_service = CommonService()
        self.user_database = {
            "admin@example.com": self.common_service.hash_password("password")
        }

    def login(self, username, password):
        """Handles user login."""
        if username not in self.user_database:
            print("Error: User not found. Please register first.")
            return
        
        hashed_input_password = self.common_service.hash_password(password)
        
        if self.user_database[username] == hashed_input_password:
            print("Login successful!")
        else:
            print("Error: Incorrect password.")
