import base64
from shared.domain.entities.user import User
from shared.domain.enum.roles_enum import Role
from shared.exceptions.user.not_found_exception import UserNotFoundException
from shared.ports.secondary.authenticator_protocol import AuthenticatorProtocol
from shared.ports.secondary.user_repository_protocol import UserRepositoryProtocol


class BasicAuthenticator(AuthenticatorProtocol):
    def __init__(self, user_repository: UserRepositoryProtocol):
        self.user_repository = user_repository

    def authenticate(self, token: str) -> User:
        decoded = base64.b64decode(token).decode("utf-8")
        email, password = decoded.split(":")

        user = self.user_repository.find_by_email(email)
        if not user:
            raise UserNotFoundException(email)

        return user