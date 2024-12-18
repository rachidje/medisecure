from domain.entities.patient import Patient
from domain.ports.patient_repository_protocol import PatientRepositoryProtocol


class InMemoryPatientRepository(PatientRepositoryProtocol):
    def __init__(self):
        self.patients: list[Patient] = []

    def create(self, patient: Patient) -> None:
        self.patients.append(patient)

    def find_by_email(self, email: str) -> Patient | None:
        for patient in self.patients:
            if patient.email == email:
                return patient
        return None