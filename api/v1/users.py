from fastapi import APIRouter,Depends,status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from typing import Annotated


from core import get_db
from core.dependencies import token_verify_middleware
from crud import CRUDUsersInstance
from schemas.users import UserCreate,LoginResponse
from core.token import authenticate_user,create_access_token,oauth2_scheme
from utils.app_exception import AppException

password_context=CryptContext(schemes=['bcrypt'],deprecated="auto")

user_router = APIRouter(tags=['USER'])

@user_router.get('/',dependencies=[Depends(token_verify_middleware),Depends(oauth2_scheme)])
def get_all_users(db:Session = Depends(get_db)):
    roles = CRUDUsersInstance.get_all_record(db)
    return roles

@user_router.post('/', dependencies=[Depends(token_verify_middleware),Depends(oauth2_scheme)])
def create_user(req:UserCreate,db:Session=Depends(get_db)):
    req.password = password_context.hash(req.password)
    new_user = CRUDUsersInstance.create(db,req)
    return new_user

@user_router.post('/login', response_model=LoginResponse)
async def login(body: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = authenticate_user(db=db, username=body.username, password=body.password)
    if not user:
        # return {"status":0,"message":"Incorrect username or password"}
        raise AppException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
            data={}
        )
    access_token = create_access_token(data={"user_id": str(user.id),})

    return {"user": jsonable_encoder(user), "access_token": access_token}