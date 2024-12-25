from datetime import date
from typing import Any
from sqlalchemy import Boolean, Date, String
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

from shared.adapters.secondary.mysql_db.connection import get_engine

Base: Any = declarative_base()
engine = get_engine()

class PatientModel(Base):
    __tablename__ = "patient"

    id:                Mapped[str] = mapped_column(String(500), primary_key=True, index=True)
    firstname:         Mapped[str] = mapped_column(String(500), nullable=False)
    lastname:          Mapped[str] = mapped_column(String(500), nullable=False)
    email:             Mapped[str] = mapped_column(String(500), nullable=False)
    date_of_birth:     Mapped[date] = mapped_column(Date, nullable=False)
    consent:           Mapped[bool] = mapped_column(Boolean, nullable=False)
    guardian_consent:  Mapped[bool] = mapped_column(Boolean, nullable=False)
    created_by:        Mapped[str] = mapped_column(String(500), nullable=False)

Base.metadata.create_all(engine)