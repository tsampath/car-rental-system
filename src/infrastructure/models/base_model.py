from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer
from sqlalchemy.schema import Sequence

Base = declarative_base()

class BaseModel(Base):
    """Base model for all database models with an auto-increment primary key starting from 1000."""
    __abstract__ = True

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_auto_increment': '1000'  # Auto-increment initial value
    }
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
