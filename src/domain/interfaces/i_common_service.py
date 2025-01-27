from abc import ABC, abstractmethod
from typing import Any, List

class ICommonService(ABC):
    """
    An abstract base class ICommonService serving as a 'repository interface'
    """

    @abstractmethod
    def hash_password(self, password) -> Any:
        """
        Hash password persist
        """
        pass

    @abstractmethod
    def validate_email(self, email) -> bool:
        """
        Validate given string as Email.
        """
        pass

    @abstractmethod
    def validate_date(self, date) -> bool:
        """
        Validate given string as date.
        """
        pass
