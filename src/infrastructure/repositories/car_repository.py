from typing import List

from infrastructure.models.car_model import CarModel
from domain.entities.car_entity import CarEntity
from domain.interfaces.i_car_repository import ICarRepository
from .base_repository import BaseRepository

class CarRepository(BaseRepository[CarModel, CarEntity], ICarRepository):
    """Repository for CarModel."""

    def __init__(self, session):
        super().__init__(CarModel, session)

    def get_by_make(self, make: str) -> List[CarEntity]:
        """Retrieve a Car by make."""
        records = self.session.query(CarModel).filter_by(make = make)
        return [self.to_entity(record) for record in records]
        # return self.to_entity(record) if record else None
    
    def get_by_model(self, model: str) -> List[CarEntity]:
        """Retrieve a Car by make."""
        records = self.session.query(CarModel).filter_by(model = model)
        return [self.to_entity(record) for record in records]
        
    def get_by_year(self, year: str) -> List[CarEntity]:
        """Retrieve a Car by make."""
        records = self.session.query(CarModel).filter_by(year = year)
        return [self.to_entity(record) for record in records]
        
    def get_by_car_id(self, car_id: str) -> CarEntity:
        """Retrieve a Car by Car Id."""
        record = self.session.query(CarModel).filter_by(car_id = car_id).first()
        return self.to_entity(record) if record else None
    
    def get_by_availability(self, is_available: bool) -> List[CarEntity]:
        """Retrieve a Car by availability."""
        records = self.session.query(CarModel).filter_by(availability = is_available)
        return [self.to_entity(record) for record in records]
        
    def to_model(self, entity: CarEntity) -> CarModel:
        """Convert CarEntity to CarModel."""
        return CarModel(
            id=entity.to_binary_id(),
            car_id=entity.car_id,
            make=entity.make,
            model=entity.model,
            year=entity.year,
            mileage=entity.mileage,
            availability=entity.availability,
            minimum_rent_period=entity.minimum_rent_period,
            maximum_rent_period=entity.maximum_rent_period,
        )

    def to_entity(self, model: CarModel) -> CarEntity:
        """Convert CarModel to CarEntity."""
        return CarEntity(
            id=CarEntity.from_binary_id(model.id),
            car_id=model.car_id,
            make=model.make,
            model=model.model,
            year=model.year,
            mileage=model.mileage,
            availability=model.availability,
            minimum_rent_period=model.minimum_rent_period,
            maximum_rent_period=model.maximum_rent_period
        )
