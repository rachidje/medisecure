import pytest

from patient_management.infrastructure.adapter.secondary.mysql.mysql_patient_repository\
    import MySQLPatientRepository
from patient_management.tests.e2e.seeds.patient_seeds import E2ePatients
from shared.adapters.secondary.mysql_db.connection import get_session
from shared.tests.test_app import TestApp


@pytest.mark.int
class TestIntMySQLPatientRepository:
    # pylint: disable=W0201
    def setup_method(self):
        self.test_app = TestApp()
        self.test_app.setup()
        session = get_session()

        self.patient_repository = MySQLPatientRepository(session)

    def test_should_create_patient(self):
        self.patient_repository.create(E2ePatients.alice.entity)

        fetched_patient = self.patient_repository.find_by_id(E2ePatients.alice.entity.id)
        assert fetched_patient is not None
        assert fetched_patient.id == E2ePatients.alice.entity.id
