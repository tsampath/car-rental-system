# Initialize database
from infrastructure.db.mysql_db_connection import DB_Connection
from infrastructure.models.user_model import UserModel
from infrastructure.models.car_model import CarModel

class Startup:

    def __init__(self):
        engine = DB_Connection().get_engine()
        UserModel.metadata.create_all(bind=engine)
        CarModel.metadata.create_all(bind=engine)
