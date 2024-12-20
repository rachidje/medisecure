from sqlalchemy.orm import Session

from patient_management.domain.entities.patient import Patient
from patient_management.domain.entities.patient_model import PatientModel
from patient_management.domain.ports.patient_repository_protocol import PatientRepositoryProtocol


class MySQLPatientRepository(PatientRepositoryProtocol):
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, patient: Patient) -> None:
        model = PatientModel(
            id = patient.id,
            firstname = patient.firstname,
            lastname = patient.lastname,
            email= patient.email,
            date_of_birth = patient.date_of_birth,
            consent = patient.consent,
            guardian_consent = patient.guardian_consent,
            created_by = patient.created_by
        )
        self.session.add(model)
        self.session.commit()
    
    def find_by_id(self, id: str) -> Patient | None:
        model = self.session.query(PatientModel).filter_by(id= id).first()
        
        return Patient(
            id= model.id,
            firstname= model.firstname,
            lastname= model.lastname,
            email= model.email,
            date_of_birth= model.date_of_birth,
            consent= model.consent,
            guardian_consent= model.guardian_consent,
            created_by= model.created_by
        ) if model else None

    def find_by_email(self, email: str) -> Patient | None:
        model = self.session.query(PatientModel).filter_by(email= email).first()
        
        return Patient(
            id= model.id,
            firstname= model.firstname,
            lastname= model.lastname,
            email= model.email,
            date_of_birth= model.date_of_birth,
            consent= model.consent,
            guardian_consent= model.guardian_consent,
            created_by= model.created_by
        ) if model else None
        
