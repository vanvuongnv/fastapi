
import os
from dotenv import load_dotenv


load_dotenv()

def get_connection_string():
    engine = os.environ.get('DB_ENGINE')
    dbhost = os.environ.get('DB_HOST')
    dbport = os.environ.get('DB_PORT')
    username = os.environ.get('DB_USERNAME')
    password = os.environ.get('DB_PASSWORD')
    dbname = os.environ.get('DB_NAME')
    return f'{engine}://{username}:{password}@{dbhost}:{dbport}/{dbname}'

# database configurations
SQLALCHEMY_DATABASE_URL = get_connection_string()
ADMIN_DEFAULT_PASSWORD = os.environ.get('DEFAULT_PASSWORD')

# JWT configurations
JWT_SECRET = os.environ.get('JWT_SECRET')
JWT_ALGORITHM = os.environ.get('JWT_ALGORITHM')