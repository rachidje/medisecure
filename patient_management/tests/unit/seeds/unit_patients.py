
from datetime import date
from patient_management.application.usecases.create_patient_folder_usecase import PatientDataPayload
from patient_management.tests.unit.seeds.unit_users import UnittestUsers


class UnittestPatients:
    john_doe: PatientDataPayload = {
        "firstname": "Alice",
        "lastname": "Bowman",
        "email": "alice.bowman@example.com",
        "date_of_birth": date(1990, 1, 1),
        "consent": True,
        "guardian_consent": True,
        "medical_professional": UnittestUsers.medical_professional
    } 