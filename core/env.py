from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv('.env'))

SECRET_KEY: str = getenv('SECRET_KEY')
ALGORITHM: str = getenv('ALGORITHM')
TIME: int = int(getenv('ACCESS_TOKEN_EXPIRE_DAYS'))