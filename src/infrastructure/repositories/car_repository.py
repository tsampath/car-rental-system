from typing import List
from datetime import date
from sqlalchemy import and_, or_, select

from infrastructure.models.car_model import CarModel
from infrastructure.models.booking_model import BookingModel
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
    
    def search_available_cars(self, start_date: date, end_date: date) -> List[CarEntity]:
        """Retrieve available cars that are not booked within the given date range and
        have a rental period within their min/max rental period limits."""

        # Calculate the booking duration
        num_days = (end_date - start_date).days

        # Subquery: Find all cars that have overlapping bookings
        booked_cars_subquery = select(BookingModel.car_id).where(
            and_(
                BookingModel.is_closed == False,  # Active bookings only
                or_(
                    and_(BookingModel.booking_start_date <= start_date, BookingModel.booking_end_date >= start_date),  # New start overlaps existing booking
                    and_(BookingModel.booking_start_date <= end_date, BookingModel.booking_end_date >= end_date),  # New end overlaps existing booking
                    and_(BookingModel.booking_start_date >= start_date, BookingModel.booking_end_date <= end_date)  # Existing booking inside new range
                )
            )
        )

        # Query available cars
        available_cars = self.session.query(CarModel).filter(
            ~CarModel.id.in_(booked_cars_subquery),  # Exclude booked cars
            CarModel.minimum_rent_period <= num_days,  # Ensure min rent period
            CarModel.maximum_rent_period >= num_days  # Ensure max rent period
        ).all()

        return [self.to_entity(car) for car in available_cars]

    def is_car_available(self, car_id: int, start_date: date, end_date: date) -> bool:
        """Check whether that the given car is available or not depending on given dates"""

        # Calculate booking duration in days
        num_days = (end_date - start_date).days

        # Check if the car exists
        car = self.session.query(CarModel).filter(CarModel.id == car_id).first()
        if not car:
            return False  # Car doesn't exist

        # Ensure booking duration is within allowed range
        if num_days < car.minimum_rent_period or num_days > car.maximum_rent_period:
            return False  # Rental period constraints not met

         # Check if the car is already booked during the requested period
        overlapping_bookings = self.session.query(BookingModel.id).filter(
            BookingModel.car_id == car_id,
            BookingModel.is_closed == False,
            or_(
                and_(BookingModel.booking_start_date <= start_date, BookingModel.booking_end_date >= start_date),  # New start overlaps existing booking
                and_(BookingModel.booking_start_date <= end_date, BookingModel.booking_end_date >= end_date),  # New end overlaps existing booking
                and_(BookingModel.booking_start_date >= start_date, BookingModel.booking_end_date <= end_date)  # Existing booking inside new range
            )
        ).count()

        return overlapping_bookings == 0  # Car is available if there are no active bookings
        
    def to_model(self, entity: CarEntity) -> CarModel:
        """Convert CarEntity to CarModel."""
        return CarModel(
            id=entity.id,
            car_id=entity.car_id,
            make=entity.make,
            model=entity.model,
            year=entity.year,
            mileage=entity.mileage,
            availability=entity.availability,
            minimum_rent_period=entity.minimum_rent_period,
            maximum_rent_period=entity.maximum_rent_period,
            created_at = entity.created_at,
            updated_at = entity.updated_at
        )

    def to_entity(self, model: CarModel) -> CarEntity:
        """Convert CarModel to CarEntity."""
        return CarEntity(
            id=model.id,
            car_id=model.car_id,
            make=model.make,
            model=model.model,
            year=model.year,
            mileage=model.mileage,
            availability=model.availability,
            minimum_rent_period=model.minimum_rent_period,
            maximum_rent_period=model.maximum_rent_period,
            created_at=model.created_at,
            updated_at=model.updated_at
        )
