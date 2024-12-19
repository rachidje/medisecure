from datetime import date
from pydantic import BaseModel


class Patient(BaseModel):
    id: str
    firstname: str
    lastname: str
    email: str
    date_of_birth: date
    consent: bool
    guardian_consent: bool
    created_by: str

    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
    
    def is_minor(self):
        return self.age < 18