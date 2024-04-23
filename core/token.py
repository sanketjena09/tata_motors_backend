from jose import  jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi.encoders import jsonable_encoder
from datetime import datetime, timedelta,UTC

from models.users import Users
from crud import CRUDUsersInstance
from . import password_context
from .env import TIME, ALGORITHM, SECRET_KEY

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/users/login")

def verify_password(plain_password, hashed_password):   
    return password_context.verify(plain_password, hashed_password)
 
def hash_password(password:str):
    return password_context.hash(password)

def authenticate_user(db, username: str, password: str):
    user = CRUDUsersInstance.get_user_login(db,user_name = username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta = timedelta(days=TIME)):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
