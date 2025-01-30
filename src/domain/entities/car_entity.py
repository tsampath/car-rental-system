from domain.entities.base_entity import BaseEntity

class CarEntity(BaseEntity):
    """User DTO with Pydantic validation."""
    car_id: str
    make: str
    model: str
    year: int
    mileage: int
    availability: bool
    minimum_rent_period: int
    maximum_rent_period: int

    class Config:
        from_attributes = True
