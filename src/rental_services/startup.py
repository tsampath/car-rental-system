# Initialize database
from infrastructure.db.mysql_db_connection import DB_Connection
from infrastructure.models.user_model import UserModel
from infrastructure.models.car_model import CarModel
from infrastructure.models.customer_model import CustomerModel
from infrastructure.models.booking_model import BookingModel

class Startup:

    def __init__(self):
        engine = DB_Connection().get_engine()
        UserModel.metadata.create_all(bind=engine)
        CarModel.metadata.create_all(bind=engine)
        CustomerModel.metadata.create_all(bind=engine)
        BookingModel.metadata.create_all(bind=engine)
