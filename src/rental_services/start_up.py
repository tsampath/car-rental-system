# Initialize database
from infrastructure.db.mysql_db_connection import DB_Connection
from infrastructure.models.user import User

class StartUp:

    def __init__(self):
        pass
        engine = DB_Connection().get_engine()
        User.metadata.create_all(bind=engine)
