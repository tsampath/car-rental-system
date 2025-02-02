import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Integer, DateTime, func

class BaseModel():
    """Base model for all database models with an auto-increment primary key starting from 1000."""
    __abstract__ = True

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_auto_increment': '1000'  # Auto-increment initial value
    }
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
