from typing import List
from datetime import datetime, timezone, timedelta

from infrastructure.models.booking_model import BookingModel
from domain.entities.booking_entity import BookingEntity
from domain.interfaces.i_booking_repository import IBookingRepository
from .base_repository import BaseRepository

class BookingRepository(BaseRepository[BookingModel, BookingEntity], IBookingRepository):
    """Repository for BookingModel."""

    def __init__(self, session):
        super().__init__(BookingModel, session)

    def close_booking_by_id(self, booking_id: int) -> bool:
        """Mark a booking as closed."""
        booking = self.session.query(BookingModel).filter_by(id=booking_id).first()
        if booking:
            booking.updated_at = datetime.now(timezone.utc)
            booking.closed_date = datetime.now(timezone.utc)
            booking.is_closed = True
            self.session.commit()
            return True
        return False
    
    def get_opened_bookings(self) -> List[BookingEntity]:
        """Retrieve opened bookings."""
        records = self.session.query(BookingModel).filter_by(is_closed = False)
        return [self.to_entity(record) for record in records]

    def get_opened_booking_by_car(self, car_id: int) -> List[BookingEntity]:
        """Retrieve an active (not closed) booking for a specific car."""
        bookings = self.session.query(BookingModel).filter(
            BookingModel.car_id == car_id, BookingModel.is_closed == False
        ).all()
        return [self.to_entity(record) for record in bookings]

    def get_opened_bookings_by_customer(self, customer_id: int) -> List[BookingEntity]:
        """Retrieve all active (not closed) bookings for a specific customer."""
        bookings = self.session.query(BookingModel).filter(
            BookingModel.customer_id == customer_id, BookingModel.is_closed == False
        ).all()

        return [self.to_entity(booking) for booking in bookings]
    
    def get_closed_bookings_by_days(self, number_of_days: int) -> List[BookingEntity]:
        """Retrieve all closed bookings within the last requested days."""
        givenDate = datetime.now(timezone.utc) - timedelta(days=number_of_days)
        
        closed_bookings = self.session.query(BookingModel).filter(
            BookingModel.is_closed == True,
            BookingModel.closed_date >= givenDate
        ).all()

        return [self.to_entity(booking) for booking in closed_bookings]
    
    def to_model(self, entity: BookingEntity) -> BookingModel:
        """Convert BookingEntity to BookingModel."""
        return BookingModel(
            id=entity.id,
            car_id=entity.car_id,
            customer_id=entity.customer_id,
            booking_start_date=entity.booking_start_date,
            booking_end_date=entity.booking_end_date,
            is_closed=entity.is_closed,
            closed_date=entity.closed_date,
            additional_comment=entity.additional_comment,
            created_at = entity.created_at,
            updated_at = entity.updated_at
        )

    def to_entity(self, model: BookingModel) -> BookingEntity:
        """Convert BookingModel to BookingEntity."""
        return BookingEntity(
            id=model.id,
            car_id=model.car_id,
            customer_id=model.customer_id,
            booking_start_date=model.booking_start_date,
            booking_end_date=model.booking_end_date,
            is_closed=model.is_closed,
            closed_date=model.closed_date,
            additional_comment=model.additional_comment,
            created_at=model.created_at,
            updated_at=model.updated_at
        )
