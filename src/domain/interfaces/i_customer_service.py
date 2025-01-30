from abc import ABC, abstractmethod
from typing import List
from domain.entities.customer_entity import CustomerEntity

class ICustomerService(ABC):
    """Interface for CustomerService."""

    @abstractmethod
    def add_customer(self, customer_entity: CustomerEntity) -> CustomerEntity:
        """Add a new customer."""
        pass

    @abstractmethod
    def get_all_customers(self) -> List[CustomerEntity]:
        """Retrieve all customers."""
        pass

    @abstractmethod
    def get_customer_by_id(self, id: int) -> CustomerEntity:
        """Retrieve a customer by ID."""
        pass

    @abstractmethod
    def delete_customer_by_id(self, id: int) -> bool:
        """Delete a customer by ID."""
        pass

    @abstractmethod
    def update_customer_by_id(self, id: int, customer_entity: CustomerEntity) -> CustomerEntity:
        """Update a customer by ID."""
        pass

    @abstractmethod
    def get_customers_by_name(self, name: str) -> List[CustomerEntity]:
        """Retrieve a customer by name."""
        pass

    @abstractmethod
    def get_customers_by_type(self, type_id: str) -> List[CustomerEntity]:
        """Retrieve a customer by type."""
        pass

    @abstractmethod
    def get_customers_by_price_list(self, price_list_id: str) -> List[CustomerEntity]:
        """Retrieve a customer by list."""
        pass
