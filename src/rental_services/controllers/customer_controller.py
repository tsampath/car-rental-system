from typing import List

from domain.services.common_service import CommonService
from domain.entities.customer_entity import CustomerEntity
from domain.services.customer_service import CustomerService
from rental_services.service_locator import ServiceLocator

class CustomerController:
    """Controller for customer registration and related operations."""

    def __init__(self):
        self.common_service = CommonService()

        """Initialize CustomerController with CustomerService."""
        self.customer_service: CustomerService = ServiceLocator.get_customer_service()
        
        # Add customer
    def add_customer(self, customer_data: dict) -> CustomerEntity:        
        
        # Validate email
        if not self.common_service.validate_email(customer_data['email']):
            print("Error: Invalid email format. Please enter a valid email.")
            return
        
        new_customer = CustomerEntity(
            name = customer_data['name'],
            building_name = customer_data['building_name'],
            address_line_1 = customer_data['address_line_1'],
            address_line_2 = customer_data['address_line_2'],
            town = customer_data['town'],
            customer_type_id = customer_data['customer_type_id'],
            price_list_id = customer_data['price_list_id'],
            email=customer_data['email']
        )
        print("Customer successful added!")
        return self.customer_service.add_customer(new_customer)

    def get_all_customers(self) -> List[CustomerEntity]:
        """Get all registered customers."""
        return self.customer_service.get_all_customers()

    def get_customer_by_id(self, id: int):
        """Get a customer by ID."""
        return self.customer_service.get_customer_by_id(id)
    
    def delete_customer_by_id(self, id: int):
        """Delete a customer by ID."""
        return self.customer_service.delete_customer_by_id(id)

    def update_customer_by_id(self, id: int, customer_data: dict):
        """Update a customer by ID."""

        # Validate email
        if not self.common_service.validate_email(customer_data['email']):
            print("Error: Invalid email format. Please enter a valid email.")
            return

        return self.customer_service.update_customer_by_id(id, CustomerEntity(**customer_data))

    def get_customer_by_name(self, name: str) -> List[CustomerEntity]:
        """Get a customer by Name."""
        return self.customer_service.get_customers_by_name(name)

    def get_customers_by_type(self, type_id: int) -> List[CustomerEntity]:
        """Get a customers by Type."""
        return self.customer_service.get_customers_by_type(type_id)

    def get_customers_by_price_list(self, price_list_id: int) -> List[CustomerEntity]:
        """Get a customers by price list"""
        return self.customer_service.get_customers_by_price_list(price_list_id)
   
