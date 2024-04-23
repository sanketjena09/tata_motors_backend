from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from core import get_db
from core.dependencies import token_verify_middleware
from core.token import oauth2_scheme
from crud import CRUDRoleInstance
from schemas.role import RoleCreate

role_router = APIRouter(tags=['ROLE'])

@role_router.get('/')
def get_all_role(db:Session = Depends(get_db)):
    roles = CRUDRoleInstance.get_all_record(db)
    return roles

@role_router.post('/',dependencies=[Depends(token_verify_middleware),Depends(oauth2_scheme)])
def create_role(req:RoleCreate,db:Session=Depends(get_db)):
    new_role = CRUDRoleInstance.create(db,req)
    return new_role