from patient_management.domain.ports.role_policy_protocol import RolePolicyProtocol
from shared.domain.enum.roles_enum import Role


class BasePolicy(RolePolicyProtocol):
    allowed_roles: list[Role] = []

    def is_allowed(self, role: list[Role]) -> bool:
        return any(role in self.allowed_roles for role in role)