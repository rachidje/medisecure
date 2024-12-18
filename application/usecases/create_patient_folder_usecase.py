from typing import TypedDict
from domain.exceptions.patient_already_exist_exception import PatientAlreadyExistsException
from domain.ports.patient_repository_protocol import PatientRepositoryProtocol

class PatientDataPaylod(TypedDict):
    firstname: str
    lastname: str
    email: str


class CreatePatientFolderUseCase:
    def __init__(self, repository: PatientRepositoryProtocol):
        self.repository = repository

    def execute(self, payload: PatientDataPaylod):
        existing_patient = self.repository.find_by_email(payload["email"])
        if existing_patient:
            raise PatientAlreadyExistsException(existing_patient.email)

