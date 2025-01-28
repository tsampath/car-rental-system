from domain.interfaces.i_car_service import ICarService
from domain.interfaces.i_car_repository import ICarRepository
from domain.entities.car_entity import CarEntity

class CarService(ICarService):
    """Service layer for Car operations."""

    def __init__(self, car_repository: ICarRepository):
        """Initialize CarService with a CarRepository instance."""
        self.car_repository = car_repository

    def add_car(self, car_entity: CarEntity) -> CarEntity:
        """Add a new car."""
        return self.car_repository.add(car_entity)

    def get_all_cars(self):
        """Retrieve all cars."""
        return self.car_repository.get_all()

    def get_car_by_id(self, id: str) -> CarEntity:
        """Retrieve a car by ID."""
        return self.car_repository.get_by_id(id)

    def delete_car_by_id(self, id: str) -> bool:
        """Delete a car by ID."""
        return self.car_repository.delete_by_id(id)

    def update_car_by_id(self, id: str, car_entity: CarEntity) -> CarEntity:
        """Update a car by ID."""
        return self.car_repository.update_by_id(id, car_entity)

    def get_car_by_car_id(self, car_id: str) -> CarEntity:
        """Retrieve a car by make."""
        return self.car_repository.get_by_car_id(car_id)

    def get_by_make(self, make: str) -> CarEntity:
        """Retrieve a car by make."""
        return self.car_repository.get_by_make(make)

    def get_car_by_model(self, model: str) -> CarEntity:
        """Retrieve a car by model."""
        return self.car_repository.get_by_model(model)

    def get_car_by_year(self, year: str) -> CarEntity:
        """Retrieve a car by email."""
        return self.car_repository.get_by_year(year)
