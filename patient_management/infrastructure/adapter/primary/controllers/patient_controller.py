from patient_management.application.usecases.create_patient_folder_usecase import CreatePatientFolderUseCase, PatientDataPayload
from patient_management.infrastructure.adapter.secondary.in_memory_patient_repository import InMemoryPatientRepository
from shared.adapters.secondary.uuid_generator import UUIDGenerator


class PatientController:
    def __init__(self) -> None:
        self.repository = InMemoryPatientRepository()
        self.id_generator = UUIDGenerator()
        self.usecase = CreatePatientFolderUseCase(self.repository, self.id_generator)

    def create(self, payload: PatientDataPayload):
        return self.usecase.execute(payload)