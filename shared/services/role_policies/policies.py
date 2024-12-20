from shared.domain.enum.roles_enum import Role
from shared.services.role_policies.base_policy import BasePolicy


class DoctorPolicy(BasePolicy):
    allowed_roles = [Role.DOCTOR]

class NursePolicy(BasePolicy):
    allowed_roles = [Role.NURSE]

class AdminPolicy(BasePolicy):
    allowed_roles = [Role.ADMIN]

class LaboratoryPolicy(BasePolicy):
    allowed_roles = [Role.LAB_TECHNICIAN]