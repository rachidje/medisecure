import pytest
from api.main import container

@pytest.mark.unittest
class TestDependencyInjectionContainer:
    def test_should_have_same_instances(self):
        user_repo_1 = container.user_repository()
        user_repo_2 = container.user_repository()

        assert id(user_repo_1) == id(user_repo_2)

        patient_repo_1 = container.patient_repository()
        patient_repo_2 = container.patient_repository()

        assert id(patient_repo_1) == id(patient_repo_2)

        authenticator_1 = container.authenticator()
        authenticator_2 = container.authenticator()

        assert id(authenticator_1) == id(authenticator_2)
