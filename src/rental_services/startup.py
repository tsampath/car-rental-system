# Initialize database
from infrastructure.db.mysql_db_connection import DB_Connection
from infrastructure.models.user_model import UserModel

class Startup:

    def __init__(self):
        engine = DB_Connection().get_engine()
        UserModel.metadata.create_all(bind=engine)
