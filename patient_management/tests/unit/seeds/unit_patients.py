
from datetime import date
from patient_management.application.usecases.create_patient_folder_usecase import PatientDataPayload


class UnittestPatients:
    john_doe: PatientDataPayload = {
        "firstname": "John",
        "lastname": "Doe",
        "email": "john.doe@example.com",
        "date_of_birth": date(1990, 1, 1),
        "consent": True,
        "guardian_consent": True
    } 