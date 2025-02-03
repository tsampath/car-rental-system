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
            cls._engine = create_engine(
                db_url, 
                pool_size=10,               # Maintain 10 persistent connections
                max_overflow=5,             # Allow up to 5 temporary connections beyond pool_size
                pool_recycle=3600,          # Recycle connections every 1 hour (3600 seconds)
                pool_timeout=30,            # Wait 30 seconds before raising timeout errors
                pool_pre_ping=True          # Test the connection before using it
            )
            cls._Session = sessionmaker(autocommit=False, autoflush=False, bind=cls._engine)
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
