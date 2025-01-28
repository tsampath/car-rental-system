from abc import ABC, abstractmethod
from typing import List
from domain.entities.car_entity import CarEntity

class ICarRepository(ABC):
    """Interface for CarRepository."""

    @abstractmethod
    def add(self, Car_model: CarEntity) -> CarEntity:
        """Add a new Car."""
        pass

    @abstractmethod
    def get_all(self) -> List[CarEntity]:
        """Retrieve all Cars."""
        pass

    @abstractmethod
    def get_by_id(self, Car_id: str) -> CarEntity:
        """Retrieve a Car by ID."""
        pass

    @abstractmethod
    def delete_by_id(self, Car_id: str) -> bool:
        """Delete a Car by ID."""
        pass

    @abstractmethod
    def update_by_id(self, Car_id: str, Car_model: CarEntity) -> CarEntity:
        """Update a Car by ID."""
        pass

    @abstractmethod
    def get_by_make(self, make: str) -> CarEntity:
        """Retrieve a Car by make."""
        pass

    @abstractmethod
    def get_by_car_id(self, car_id: str) -> CarEntity:
        """Retrieve a Car by car_id."""
        pass

    @abstractmethod
    def get_by_model(self, model: str) -> CarEntity:
        """Retrieve a Car by model."""
        pass

    @abstractmethod
    def get_by_year(self, year: str) -> CarEntity:
        """Retrieve a Car by year."""
        pass

    @abstractmethod
    def to_model(self, entity: CarEntity):
        """Convert a CarEntity to a CarModel."""
        pass

    @abstractmethod
    def to_entity(self, model) -> CarEntity:
        """Convert a CarModel to a CarEntity."""
        pass
