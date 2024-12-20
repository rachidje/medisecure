import pytest

from patient_management.tests.unit.seeds.unit_users import UnittestUsers
from shared.adapters.secondary.in_memory_user_repository import InMemoryUserRepository
from shared.services.authenticator.basic_authenticator import BasicAuthenticator


@pytest.mark.unittest
class TestBasicAuthenticator:
    def setup_method(self):
        self.user_repository = InMemoryUserRepository()
        self.authenticator = BasicAuthenticator(self.user_repository)
        self.user_repository.create(
            UnittestUsers.medical_professional
        )

    def test_should_return_user(self):
        token = "am9obmRvZUBnbWFpbC5jb206cXdlcnR5"
        user = self.authenticator.authenticate(token)

        assert user.email == 'johndoe@gmail.com'
        assert user.password == 'qwerty'