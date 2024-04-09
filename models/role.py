
from sqlalchemy import TEXT, INT, FLOAT, DATE, Column,Uuid,VARCHAR,Enum,JSON,TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from typing import Text

from models.base_model import BaseModel as Base



class Role(Base):
    __tablename__ = "role"
    name: Mapped[TEXT] = mapped_column(TEXT)

    def __init__(self, **kw: any):
        super().__init__(**kw)
        