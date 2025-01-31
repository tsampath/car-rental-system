import hashlib
import re
from datetime import datetime

class CommonService:
    """Service providing common utilities like hashing and validation."""

    @staticmethod
    def hash_password(password: str) -> str:
        """Hashes a password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validates email format."""
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

    @staticmethod
    def validate_date(date: str) -> bool:
        """Validates a date format (YYYY-MM-DD) and checks if it's a real date."""
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            return False        
