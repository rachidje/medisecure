from datetime import date
from patient_management.domain.entities.patient import Patient
from patient_management.tests.e2e.fixtures.patient_fixture import PatientFixture
from shared.tests.fixtures.seeds.user_seeds import E2eUsers


class E2ePatients:
    alice = PatientFixture(
        Patient(
            id = "alice",
            email = "alice@gmail.com",
            firstname = "Alice",
            lastname = "Doe",
            date_of_birth = date(1990, 1, 1),
            consent = True,
            guardian_consent = False,
            created_by = E2eUsers.doctor.entity.id
        )
    )

    minor = PatientFixture(
        Patient(
            id = "minor",
            email = "minor@gmail.com",
            firstname = "Minor",
            lastname = "Doe",
            date_of_birth = date(2014, 1, 1),
            consent = False,
            guardian_consent = True,
            created_by = E2eUsers.doctor.entity.id
        )
    )