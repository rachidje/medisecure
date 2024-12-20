from patient_management.application.usecases.create_patient_folder_usecase import CreatePatientFolderUseCase, PatientDataPayload
from shared.domain.enum.roles_enum import Role
from shared.exceptions.user.unauthorized_role_exception import UnauthorizedRoleException


class PatientController:
    def __init__(self, usecase: CreatePatientFolderUseCase) -> None:
        self.usecase = usecase

    def create(self, payload: PatientDataPayload):
        ALLOWED_ROLES = [Role.ADMIN, Role.DOCTOR, Role.NURSE]

        if not any(role in ALLOWED_ROLES for role in payload['medical_professional'].roles):
            raise UnauthorizedRoleException()

        return self.usecase.execute(payload)