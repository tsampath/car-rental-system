from enum import Enum

class CustomerType(Enum):
    INDIVIDUAL = 1,
    CORPORATE = 2

class PriceList(Enum):
    Standard = 1
    Loyal = 2

class BookingStatus(Enum):
    Pending = 1
    Approved = 2
