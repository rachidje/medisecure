from datetime import date
from pydantic import BaseModel


class Patient(BaseModel):
    firstname: str
    lastname: str
    email: str
    date_of_birth: date
    consent: bool