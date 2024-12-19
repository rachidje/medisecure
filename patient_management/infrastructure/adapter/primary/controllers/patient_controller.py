from patient_management.application.usecases.create_patient_folder_usecase import CreatePatientFolderUseCase, PatientDataPayload
from patient_management.infrastructure.adapter.secondary.in_memory_patient_repository import InMemoryPatientRepository
from shared.adapters.secondary.uuid_generator import UUIDGenerator
from shared.domain.enum.roles_enum import Role
from shared.exceptions.user.unauthorized_role_exception import UnauthorizedRoleException


class PatientController:
    def __init__(self) -> None:
        self.repository = InMemoryPatientRepository()
        self.id_generator = UUIDGenerator()
        self.usecase = CreatePatientFolderUseCase(self.repository, self.id_generator)

    def create(self, payload: PatientDataPayload):
        ALLOWED_ROLES = [Role.ADMIN, Role.DOCTOR, Role.NURSE]

        if not any(role in ALLOWED_ROLES for role in payload['medical_professional'].roles):
            raise UnauthorizedRoleException()

        return self.usecase.execute(payload)