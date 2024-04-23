from .base_schema import Base


class UserCreate(Base):
    name:str
    user_name:str
    password:str
    role:str

class UserRole(Base):
    id:str
    name:str

class UserResponse(Base):
    id: str
    name: str
    user_name: str
    role: UserRole

class LoginResponse(Base):
    access_token    : str
    user: UserResponse