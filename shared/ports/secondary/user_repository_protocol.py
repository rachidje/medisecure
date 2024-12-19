from typing import Protocol

from shared.domain.entities.user import User


class UserRepositoryProtocol(Protocol):
    def find_by_email(self, email: str) -> User | None: ...
    def create(self, user: User) -> None: ...