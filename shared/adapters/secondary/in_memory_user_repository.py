from shared.domain.entities.user import User
from shared.ports.secondary.user_repository_protocol import UserRepositoryProtocol


class InMemoryUserRepository(UserRepositoryProtocol):
    def __init__(self):
        self.users: list[User] = []

    def find_by_email(self, email: str) -> User | None:
        return next((user for user in self.users if user.email == email), None)

    def create(self, user: User) -> None:
        self.users.append(user)