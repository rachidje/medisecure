from pydantic import BaseModel


class PatientDTO(BaseModel):
    firstname: str
    lastname: str
    email: str
    date_of_birth: str
    consent: bool
    guardian_consent: bool