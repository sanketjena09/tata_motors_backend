from starlette.requests import Request
from fastapi import status,Depends
from sqlalchemy.orm import Session
from starlette.datastructures import MutableHeaders
from jose import jwt
from fastapi.encoders import jsonable_encoder
from datetime import datetime,UTC
from .env import SECRET_KEY,ALGORITHM

from utils.app_exception import AppException



def token_verify_middleware(request:Request):
    if "authorization" not in [k.lower() for k in request.headers.keys()]:
        raise AppException(status_code=status.HTTP_401_UNAUTHORIZED, message="Unauthorized access")
    
    decoded_token = jwt.decode(token = request.headers["authorization"].split(" ")[1], key=SECRET_KEY, algorithms=ALGORITHM)
    userId = decoded_token['user_id']
    time = decoded_token['exp']

    start_time = datetime.strptime("1970-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    
    if (datetime.now() - start_time).total_seconds() > time:
        raise AppException(status_code=status.HTTP_401_UNAUTHORIZED,message="token expired")

    newHeaders = MutableHeaders(request.headers)
    newHeaders["user"] = userId
    request._headers = newHeaders
