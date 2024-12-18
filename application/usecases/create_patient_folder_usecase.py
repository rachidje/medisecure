from datetime import date
from typing import TypedDict

from pydantic import ValidationError
from domain.entities.patient import Patient
from domain.exceptions.missing_field__exception import MissingFieldException
from domain.exceptions.patient_already_exist_exception import PatientAlreadyExistsException
from domain.ports.patient_repository_protocol import PatientRepositoryProtocol

class PatientDataPaylod(TypedDict):
    firstname: str
    lastname: str
    email: str
    date_of_birth: date


class CreatePatientFolderUseCase:
    def __init__(self, repository: PatientRepositoryProtocol):
        self.repository = repository

    def execute(self, payload: PatientDataPaylod):
        existing_patient = self.repository.find_by_email(payload["email"])
        if existing_patient:
            raise PatientAlreadyExistsException(existing_patient.email)
        
        try:
            patient = Patient(**payload)
        except ValidationError as e:
            raise MissingFieldException(str(e.errors()[0]['loc'][0]))
