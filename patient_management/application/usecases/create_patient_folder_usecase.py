from datetime import date
from typing import TypedDict

from pydantic import ValidationError
from patient_management.domain.entities.patient import Patient
from patient_management.domain.exceptions.missing_field__exception import MissingFieldException
from patient_management.domain.exceptions.patient_already_exist_exception import PatientAlreadyExistsException
from shared.domain.entities.user import User
from shared.ports.secondary.id_generator_protocol import IDGeneratorProtocol
from patient_management.domain.ports.patient_repository_protocol import PatientRepositoryProtocol
from patient_management.domain.services.patient_service import PatientService

class PatientDataPayload(TypedDict):
    medical_professional: User
    firstname: str
    lastname: str
    email: str
    date_of_birth: date
    consent: bool
    guardian_consent: bool


class CreatePatientFolderUseCase:
    def __init__(self, patient_repository: PatientRepositoryProtocol, id_generator: IDGeneratorProtocol):
        self.patient_repository = patient_repository
        self.id_generator = id_generator

    def execute(self, payload: PatientDataPayload):
        existing_patient = self.patient_repository.find_by_email(payload["email"])
        if existing_patient:
            raise PatientAlreadyExistsException(existing_patient.email)
        
        patient_id = self.id_generator.generate()
        
        try:
            patient = Patient.model_validate({
                "id": patient_id,
                "created_by": payload["medical_professional"].id,
                **payload
            })
        except ValidationError as e:
            raise MissingFieldException(str(e.errors()[0]['loc'][0]))
        
        PatientService.validate_consent(patient)
        PatientService.validate_guardian_consent(patient)
        
        self.patient_repository.create(patient)
        return patient_id

