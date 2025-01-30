from abc import ABC, abstractmethod
from typing import List
from domain.entities.customer_entity import CustomerEntity

class ICustomerRepository(ABC):
    """Interface for CustomerRepository."""

    @abstractmethod
    def add(self, customer_model: CustomerEntity) -> CustomerEntity:
        """Add a new customer."""
        pass

    @abstractmethod
    def get_all(self) -> List[CustomerEntity]:
        """Retrieve all customers."""
        pass

    @abstractmethod
    def get_by_id(self, customer_id: int) -> CustomerEntity:
        """Retrieve a customer by ID."""
        pass

    @abstractmethod
    def delete_by_id(self, customer_id: int) -> bool:
        """Delete a customer by ID."""
        pass

    @abstractmethod
    def update_by_id(self, customer_id: int, customer_model: CustomerEntity) -> CustomerEntity:
        """Update a customer by ID."""
        pass

    @abstractmethod
    def get_customer_by_customer_id(self, customer_id: int) -> CustomerEntity:
        """Retrieve a customer by customer ID."""
        pass
    
    @abstractmethod
    def get_customers_by_name(self, name: str) -> List[CustomerEntity]:
        """Retrieve a customer by name."""
        pass

    @abstractmethod
    def get_customers_by_type(self, type_id: int) -> List[CustomerEntity]:
        """Retrieve a customer by type."""
        pass

    @abstractmethod
    def get_customers_by_price_list(self, price_list_id: int) -> List[CustomerEntity]:
        """Retrieve a customer by price list."""
        pass

    @abstractmethod
    def to_model(self, entity: CustomerEntity):
        """Convert a CustomerEntity to a CustomerModel."""
        pass

    @abstractmethod
    def to_entity(self, model) -> CustomerEntity:
        """Convert a CustomerModel to a CustomerEntity."""
        pass
