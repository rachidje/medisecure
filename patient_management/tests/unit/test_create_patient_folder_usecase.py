from datetime import date
from typing import Any
import pytest

from patient_management.application.usecases.create_patient_folder_usecase\
    import CreatePatientFolderUseCase
from patient_management.domain.entities.patient import Patient
from patient_management.domain.exceptions.missing_consent_patient_exception\
    import MissingConsentPatientException
from patient_management.domain.exceptions.missing_field__exception\
    import MissingFieldException
from patient_management.domain.exceptions.missing_guardian_consent_exception\
    import MissingGuardianConsentException
from patient_management.domain.exceptions.patient_already_exist_exception\
    import PatientAlreadyExistsException
from patient_management.tests.unit.seeds.unit_users import UnittestUsers
from shared.adapters.secondary.fixed_id_generator import FixedIDGenerator
from patient_management.infrastructure.adapter.secondary.in_memory_patient_repository\
    import InMemoryPatientRepository
from patient_management.tests.unit.seeds.unit_patients import UnittestPatients


@pytest.mark.unittest
class TestCreatePatientFolderUseCase:
    # pylint: disable=W0201
    def setup_method(self):
        self.repository = InMemoryPatientRepository()
        self.id_generator = FixedIDGenerator()

        self.usecase = CreatePatientFolderUseCase(self.repository, self.id_generator)

    def execute_without_all_fields(self, payload: Any):
        self.usecase.execute(payload)

    def test_should_fail_if_patient_already_exists(self):

        self.repository.create(Patient(
            id= "1", 
            firstname= UnittestPatients.alice["firstname"],
            lastname= UnittestPatients.alice["lastname"],
            email= UnittestPatients.alice["email"],
            date_of_birth= UnittestPatients.alice["date_of_birth"],
            consent= UnittestPatients.alice["consent"],
            guardian_consent= UnittestPatients.alice["guardian_consent"],
            created_by= UnittestUsers.medical_professional.id))

        with pytest.raises(PatientAlreadyExistsException, match=f"Patient already exists with email {UnittestPatients.alice['email']}"):
            self.usecase.execute(UnittestPatients.alice)

    def test_should_fail_if_missing_fields(self):
        with pytest.raises(MissingFieldException, match= f"Missing required field: date_of_birth"):
            self.execute_without_all_fields({
                "firstname": "John",
                "lastname": "Doe",
                "email": "john.doe@example.com",
                "consent": True,
                "guardian_consent": True,
                "medical_professional": UnittestUsers.medical_professional
            })

    def test_should_fail_if_no_consent_patient(self):
        non_consented_patient = UnittestPatients.alice.copy()
        non_consented_patient["consent"] = False
        with pytest.raises(MissingConsentPatientException, match= f"Unable to create folder without consent patient"):
            self.usecase.execute(non_consented_patient)

    def test_should_fail_if_no_guardian_consent_for_minor(self):
        minor_patient = UnittestPatients.alice.copy()
        minor_patient["date_of_birth"] = date(2010, 1, 1)
        minor_patient["guardian_consent"] = False

        with pytest.raises(MissingGuardianConsentException, match= f"Unable to create folder without guardian consent for minor"):
            self.usecase.execute(minor_patient)

    def test_should_create_patient_folder(self):
        id =self.usecase.execute(UnittestPatients.alice)

        fetched_patient = self.repository.find_by_id(id)

        assert fetched_patient is not None
        assert fetched_patient.firstname == UnittestPatients.alice["firstname"]

# test
