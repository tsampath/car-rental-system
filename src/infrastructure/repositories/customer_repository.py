from typing import List

from infrastructure.models.customer_model import CustomerModel
from domain.entities.customer_entity import CustomerEntity
from domain.interfaces.i_customer_repository import ICustomerRepository
from .base_repository import BaseRepository

class CustomerRepository(BaseRepository[CustomerModel, CustomerEntity], ICustomerRepository):
    """Repository for CustomerModel."""

    def __init__(self, session):
        super().__init__(CustomerModel, session)

    def get_customer_by_customer_id(self, customer_id: str) -> CustomerEntity:
        """Retrieve a Customer by Customer Id."""
        record = self.session.query(CustomerModel).filter_by(customer_id = customer_id).first()
        return self.to_entity(record) if record else None

    def get_customers_by_name(self, name: str) -> List[CustomerEntity]:
        """Retrieve a Customer by name."""
        records = self.session.query(CustomerModel).filter_by(name = name)
        return [self.to_entity(record) for record in records]
    
    def get_customers_by_type(self, type_id: int) -> List[CustomerEntity]:
        """Retrieve a Customer by make."""
        records = self.session.query(CustomerModel).filter_by(type_id = type_id)
        return [self.to_entity(record) for record in records]
        
    def get_customers_by_price_list(self, price_list_id: int) -> List[CustomerEntity]:
        """Retrieve a Customers by price list."""
        records = self.session.query(CustomerModel).filter_by(price_list_id = price_list_id)
        return [self.to_entity(record) for record in records]
      
    def to_model(self, entity: CustomerEntity) -> CustomerModel:
        """Convert CustomerEntity to CustomerModel."""
        return CustomerModel(
            id = entity.id,
            name = entity.name,
            building_name = entity.building_name,
            address_line_1 = entity.address_line_1,
            address_line_2 = entity.address_line_2,
            town = entity.town,
            customer_type_id = entity.customer_type_id,
            price_list_id = entity.price_list_id
        )

    def to_entity(self, model: CustomerModel) -> CustomerEntity:
        """Convert CustomerModel to CustomerEntity."""
        return CustomerEntity(
            id = model.id,
            customer_id=model.id,
            name = model.name,
            building_name = model.building_name,
            address_line_1 = model.address_line_1,
            address_line_2 = model.address_line_2,
            town = model.town,
            customer_type_id = model.customer_type_id, 
            price_list_id = model.price_list_id
        )
