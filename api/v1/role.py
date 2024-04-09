from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from core import get_db
from crud import CRUDRoleInstance

role_router = APIRouter(tags=['ROLE'])

@role_router.get('/')
def get_all_roles(db:Session = Depends(get_db)):
    roles = CRUDRoleInstance.get_all_record(db)
    return roles