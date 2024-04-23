
from sqlalchemy import TEXT, INT, FLOAT, DATE, Column,Uuid,VARCHAR,Enum,JSON,TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from typing import Text

from models.base_model import BaseModel as Base



class Users(Base):
    __tablename__ = "users"
    name: Mapped[TEXT] = mapped_column(TEXT)
    user_name: Mapped[TEXT] = mapped_column(TEXT)
    password: Mapped[TEXT] = mapped_column(TEXT)
    role: Mapped[Uuid] = mapped_column(Uuid)

    def __init__(self, **kw: any):
        super().__init__(**kw)
        