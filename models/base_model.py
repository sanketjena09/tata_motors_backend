from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from sqlalchemy import Uuid,INTEGER
from datetime import datetime,UTC,timedelta


class BaseModel(DeclarativeBase):
    id: Mapped[Uuid] = mapped_column(Uuid, primary_key=True)     
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC)+ timedelta(hours=5, minutes=30))
    updated_at: Mapped[datetime] = mapped_column(default=None, nullable=True)                           