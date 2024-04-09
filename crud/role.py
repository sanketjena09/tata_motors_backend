from typing import Type
from sqlalchemy.orm import Session
from .base import CRUDBase
from models.role import Role
from schemas.role import RoleCreate



class CRUDRole(CRUDBase[Role, RoleCreate,RoleCreate]):
    
    def __init__(self) -> None:
        self.model = Role