from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer
from sqlalchemy.schema import Sequence

Base = declarative_base()

class BaseModel(Base):
    """Base model for all database models with an auto-increment primary key starting from 1000."""
    __abstract__ = True

    id = Column(Integer, Sequence('id_seq', start=1000, increment=1), primary_key=True, autoincrement=True)
