from patient_management.application.usecases.create_patient_folder_usecase import CreatePatientFolderUseCase, PatientDataPayload
from patient_management.domain.ports.role_policy_protocol import RolePolicyProtocol
from shared.exceptions.user.unauthorized_role_exception import UnauthorizedRoleException
from shared.services.role_policies.policies import AdminPolicy, DoctorPolicy, NursePolicy


class PatientController:
    def __init__(self, usecase: CreatePatientFolderUseCase) -> None:
        self.usecase = usecase
        self.policies: list[RolePolicyProtocol] = [
            DoctorPolicy(),
            NursePolicy(),
            AdminPolicy()
        ]

    def create(self, payload: PatientDataPayload):
        user = payload['medical_professional']
        if not any(policy.is_allowed(user.roles) for policy in self.policies):
            raise UnauthorizedRoleException()

        return self.usecase.execute(payload)