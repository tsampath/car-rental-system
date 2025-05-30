from abc import ABC, abstractmethod
from typing import List
from domain.entities.car_entity import CarEntity
from datetime import date

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
    def get_by_id(self, id: int) -> CarEntity:
        """Retrieve a Car by ID."""
        pass

    @abstractmethod
    def delete_by_id(self, id: int) -> bool:
        """Delete a Car by ID."""
        pass

    @abstractmethod
    def update_by_id(self, id: int, Car_model: CarEntity) -> CarEntity:
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
    def get_by_model(self, model: str) -> List[CarEntity]:
        """Retrieve a Car by model."""
        pass

    @abstractmethod
    def get_by_year(self, year: str) -> List[CarEntity]:
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

    @abstractmethod
    def search_available_cars(self, start_date: date, end_date: date) -> List[CarEntity]:
        pass

    @abstractmethod
    def is_car_available(self, car_id: int, start_date: date, end_date: date) -> bool:
        pass