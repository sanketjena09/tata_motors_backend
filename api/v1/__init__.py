from  fastapi import APIRouter
from .role import role_router
from .users import user_router

v1_router  = APIRouter()

v1_router.include_router(role_router,prefix='/role')
v1_router.include_router(user_router,prefix='/users')