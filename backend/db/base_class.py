from sqlalchemy.orm import as_declarative, Mapped
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
from datetime import datetime
from typing import Any

# Base class for all tables
@as_declarative()
class Base:
    id : Any
    created_at : Mapped[datetime] = Column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    __name__ : str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()