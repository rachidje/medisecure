from typing import Any
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import JSON, String

from shared.adapters.secondary.mysql_db.connection import get_engine
from shared.domain.enum.roles_enum import Role

Base: Any = declarative_base()
engine = get_engine()

class UserModel(Base):
    __tablename__ = "user"

    id:                Mapped[str] = mapped_column(String(500), primary_key=True, index=True)
    firstname:         Mapped[str] = mapped_column(String(500), nullable=False)
    lastname:          Mapped[str] = mapped_column(String(500), nullable=False)
    email:             Mapped[str] = mapped_column(String(500), nullable=False)
    password:          Mapped[str] = mapped_column(String(500), nullable=False)
    roles:             Mapped[list[Role]] = mapped_column(JSON, nullable=False, default=[])
    

Base.metadata.create_all(engine)
