
from domain.entities.patient import Patient
from domain.exceptions.missing_consent_patient_exception import MissingConsentPatientException
from domain.exceptions.missing_guardian_consent_exception import MissingGuardianConsentException


class PatientService:
    @staticmethod
    def validate_consent(patient: Patient):
        if not patient.consent:
            raise MissingConsentPatientException()
        
    @staticmethod
    def validate_guardian_consent(patient: Patient):
        if patient.is_minor() and not patient.guardian_consent:
            raise MissingGuardianConsentException()