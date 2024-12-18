import pytest

from application.usecases.create_patient_folder_usecase import CreatePatientFolderUseCase
from domain.entities.patient import Patient
from domain.exceptions.patient_already_exist_exception import PatientAlreadyExistsException
from infrastructure.adapter.secondary.in_memory_patient_repository import InMemoryPatientRepository


class TestCreatePatientFolderUseCase:

    def test_should_fail_if_patient_already_exists(self):
        repository = InMemoryPatientRepository()
        usecase = CreatePatientFolderUseCase(repository)

        repository.create(Patient(
            firstname="John",
            lastname="Doe",
            email="john.doe@example.com",
        ))

        with pytest.raises(PatientAlreadyExistsException, match=f"Patient already exists with email john.doe@example.com"):
            usecase.execute({
                "firstname": "John",
                "lastname": "Doe",
                "email": "john.doe@example.com",
            })