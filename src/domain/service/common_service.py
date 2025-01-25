import hashlib
import re
from datetime import datetime

class CommonService:
    """Provides common utilities."""

    def hash_password(self, password):
        """Hashes a password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def validate_email(self, email):
        """Validates email format."""
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    def validate_date(self, date):
        """Validates a date format (YYYY-MM-DD) and checks if it's a real date."""
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            return False
