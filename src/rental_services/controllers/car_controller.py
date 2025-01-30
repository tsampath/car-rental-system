from typing import List

from domain.services.common_service import CommonService
from domain.entities.car_entity import CarEntity
from domain.services.car_service import CarService
from rental_services.service_locator import ServiceLocator

class CarController:
    """Controller for car registration and related operations."""

    def __init__(self):
        self.common_service = CommonService()

        """Initialize CarController with CarService."""
        self.car_service: CarService = ServiceLocator.get_car_service()
        print("\nAdding new car...")
        
        # Add car
    def add_car(self, car_data: dict) -> CarEntity:        
        
        new_car = CarEntity(
            car_id = car_data['car_id'],
            make = car_data['make'],
            model = car_data['model'],
            year = car_data['year'],
            mileage = car_data['mileage'],
            minimum_rent_period = car_data['minimum_rent_period'],
            maximum_rent_period = car_data['maximum_rent_period'],
            availability = True
        )
        self.car_service.add_car(new_car)

        print("Car successful added!")

    def get_all_cars(self):
        """Get all registered cars."""
        return self.car_service.get_all_cars()

    def get_car_by_id(self, id: int):
        """Get a car by ID."""
        return self.car_service.get_car_by_id(id)

    def get_car_by_car_id(self, car_id: str) -> CarEntity:
        """Get a car by ID."""
        return self.car_service.get_car_by_car_id(car_id)

    def delete_car_by_id(self, id: int):
        """Delete a car by ID."""
        return self.car_service.delete_car_by_id(id)

    def update_car_by_id(self, id: int, car_data: dict):
        """Update a car by ID."""
        return self.car_service.update_car_by_id(id, CarEntity(**car_data))
    
    def get_by_make(self, make: str) -> List[CarEntity]:
        """Retrieve a car by make."""
        return self.car_service.get_by_make(make)

    def get_car_by_model(self, model: str) -> List[CarEntity]:
        """Retrieve a car by model."""
        return self.car_service.get_car_by_model(model)

    def get_car_by_year(self, year: str) -> List[CarEntity]:
        """Retrieve a car by year."""
        return self.car_service.get_car_by_year(year)    
    
    def get_car_by_availability(self, is_available: bool) -> List[CarEntity]:
        """Retrieve a car by availability."""
        return self.car_service.get_car_by_availability(is_available)