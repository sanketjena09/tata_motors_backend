from typing import Type

from sqlalchemy.orm import Session
from .base import CRUDBase
from models.users import Users
from models.role import Role
from schemas.users import UserCreate



class CRUDUsers(CRUDBase[Users, UserCreate,UserCreate]):
    
    def __init__(self) -> None:
        self.model = Users

    def get_user_login(self,db:Session,user_name):
        user = db.query(self.model,Role.name)
        print(1)
        user = user.join(Role,self.model.role == Role.id)

        user_is = user.filter(self.model.user_name == user_name).first()

        user_is[0].role = {"id":user_is[0].role,
                           "name":user_is[1]}

        return user_is[0]
