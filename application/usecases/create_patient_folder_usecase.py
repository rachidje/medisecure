from datetime import date
from typing import TypedDict

from pydantic import ValidationError
from domain.entities.patient import Patient
from domain.exceptions.missing_consent_patient_exception import MissingConsentPatientException
from domain.exceptions.missing_field__exception import MissingFieldException
from domain.exceptions.missing_guardian_consent_exception import MissingGuardianConsentException
from domain.exceptions.patient_already_exist_exception import PatientAlreadyExistsException
from domain.ports.id_generator_protocol import IDGeneratorProtocol
from domain.ports.patient_repository_protocol import PatientRepositoryProtocol

class PatientDataPaylod(TypedDict):
    firstname: str
    lastname: str
    email: str
    date_of_birth: date
    consent: bool
    guardian_consent: bool


class CreatePatientFolderUseCase:
    def __init__(self, repository: PatientRepositoryProtocol, id_generator: IDGeneratorProtocol):
        self.repository = repository
        self.id_generator = id_generator

    def execute(self, payload: PatientDataPaylod):
        existing_patient = self.repository.find_by_email(payload["email"])
        if existing_patient:
            raise PatientAlreadyExistsException(existing_patient.email)
        
        patient_id = self.id_generator.generate()
        
        try:
            patient = Patient(id=patient_id, **payload)
        except ValidationError as e:
            raise MissingFieldException(str(e.errors()[0]['loc'][0]))
        
        if patient.is_minor() and not patient.guardian_consent:
            raise MissingGuardianConsentException()
        
        if not patient.consent:
            raise MissingConsentPatientException()
        
        self.repository.create(patient)
        return patient_id

