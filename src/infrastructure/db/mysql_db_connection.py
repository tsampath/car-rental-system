from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class DB_Connection:
    """Singleton DB_Connection for managing the database connection."""
    _instance = None
    _engine = None
    _Session = None

    def __new__(cls, db_url="mysql+pymysql://rental_user:T&hvu2QM#%@172.104.141.142:3306/yoobee_car_rental"):
        if cls._instance is None:
            cls._instance = super(DB_Connection, cls).__new__(cls)
            cls._engine = create_engine(db_url, pool_pre_ping=True)
            cls._Session = sessionmaker(bind=cls._engine)
        return cls._instance

    @classmethod
    def get_session(cls):
        """Returns a new database session."""
        if cls._Session is None:
            raise RuntimeError("DB_Connection not initialized.")
        return cls._Session()

    @classmethod
    def get_engine(cls):
        """Returns the database engine."""
        if cls._engine is None:
            raise RuntimeError("DB_Connection not initialized.")
        return cls._engine
