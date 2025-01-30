from typing import List

from domain.interfaces.i_customer_service import ICustomerService
from domain.interfaces.i_customer_repository import ICustomerRepository
from domain.entities.customer_entity import CustomerEntity

class CustomerService(ICustomerService):
    """Service layer for Customer operations."""

    def __init__(self, customer_repository: ICustomerRepository):
        """Initialize CustomerService with a CustomerRepository instance."""
        self.customer_repository = customer_repository

    def add_customer(self, customer_entity: CustomerEntity) -> CustomerEntity:
        """Add a new customer."""
        return self.customer_repository.add(customer_entity)

    def get_all_customers(self) -> List[CustomerEntity]:
        """Retrieve all customers."""
        return self.customer_repository.get_all()

    def get_customer_by_id(self, id: int) -> CustomerEntity:
        """Retrieve a customer by ID."""
        return self.customer_repository.get_by_id(id)

    def delete_customer_by_id(self, id: int) -> bool:
        """Delete a customer by ID."""
        return self.customer_repository.delete_by_id(id)

    def update_customer_by_id(self, id: int, customer_entity: CustomerEntity) -> CustomerEntity:
        """Update a customer by ID."""
        return self.customer_repository.update_by_id(id, customer_entity)

    def get_customers_by_name(self, name: str) -> List[CustomerEntity]:
        """Retrieve a customer by make."""
        return self.customer_repository.get_customers_by_name(name)

    def get_customers_by_type(self, type_id: int) -> List[CustomerEntity]:
        """Retrieve a customer by make."""
        return self.customer_repository.get_customers_by_type(type_id)

    def get_customers_by_price_list(self, price_list_id: int) -> List[CustomerEntity]:
        """Retrieve a customer by model."""
        return self.customer_repository.get_customers_by_price_list(price_list_id)

