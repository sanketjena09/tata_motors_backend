from .role import CRUDRole
from .users import CRUDUsers

CRUDRoleInstance = CRUDRole()
CRUDUsersInstance = CRUDUsers()

__all__ = [
    CRUDRoleInstance,
    CRUDUsersInstance
]