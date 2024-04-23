from .deps import get_db
from passlib.context import CryptContext


password_context=CryptContext(schemes=['bcrypt'],deprecated="auto")

__all__ = [
    get_db
]