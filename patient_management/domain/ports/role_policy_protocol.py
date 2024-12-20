from typing import Protocol

from shared.domain.enum.roles_enum import Role


class RolePolicyProtocol(Protocol):
    def is_allowed(self, role: list[Role]) -> bool: ...