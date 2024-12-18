from datetime import date
from typing import Any
import pytest

from application.usecases.create_patient_folder_usecase import CreatePatientFolderUseCase
from domain.entities.patient import Patient
from domain.exceptions.missing_field__exception import MissingFieldException
from domain.exceptions.patient_already_exist_exception import PatientAlreadyExistsException
from infrastructure.adapter.secondary.in_memory_patient_repository import InMemoryPatientRepository


class TestCreatePatientFolderUseCase:
    def setup_method(self):
        self.repository = InMemoryPatientRepository()
        self.usecase = CreatePatientFolderUseCase(self.repository)

    def execute_without_all_fields(self, payload: Any):
        self.usecase.execute(payload)

    def test_should_fail_if_patient_already_exists(self):

        self.repository.create(Patient(
            firstname="John",
            lastname="Doe",
            email="john.doe@example.com",
            date_of_birth=date(1990, 1, 1),
        ))

        with pytest.raises(PatientAlreadyExistsException, match=f"Patient already exists with email john.doe@example.com"):
            self.usecase.execute({
                "firstname": "John",
                "lastname": "Doe",
                "email": "john.doe@example.com",
                "date_of_birth": date(1990, 1, 1),
            })

    def test_should_fail_if_missing_fields(self):
        with pytest.raises(MissingFieldException, match= f"Missing required field: date_of_birth"):
            self.execute_without_all_fields({
                "firstname": "John",
                "lastname": "Doe",
                "email": "john.doe@example.com",
            })