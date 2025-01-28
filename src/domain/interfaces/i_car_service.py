from abc import ABC, abstractmethod
from typing import List
from domain.entities.car_entity import CarEntity

class ICarService(ABC):
    """Interface for CarService."""

    @abstractmethod
    def add_car(self, car_entity: CarEntity) -> CarEntity:
        pass

    @abstractmethod
    def get_all_cars(self) -> List[CarEntity]:
        pass

    @abstractmethod
    def get_car_by_id(self, car_id: str) -> CarEntity:
        pass

    @abstractmethod
    def delete_car_by_id(self, car_id: str) -> bool:
        pass

    @abstractmethod
    def update_car_by_id(self, car_id: str, car_entity: CarEntity) -> CarEntity:
        pass

    @abstractmethod
    def get_by_make(self, make: str) -> CarEntity:
        pass

    @abstractmethod
    def get_car_by_model(self, model: str) -> CarEntity:
        pass

    @abstractmethod
    def get_car_by_year(self, year: str) -> CarEntity:
        pass
