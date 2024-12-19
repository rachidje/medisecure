from typing import Protocol

from shared.domain.entities.user import User


class AuthenticatorProtocol(Protocol):
    def authenticate(self, token: str) -> User: ...