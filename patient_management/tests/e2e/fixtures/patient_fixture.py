from patient_management.domain.entities.patient import Patient
from shared.container.container import Container
from shared.tests.fixtures.fixture_protocol import FixtureProtocol


class PatientFixture(FixtureProtocol):
    def __init__(self, entity: Patient):
        self.entity = entity

    def load(self, container: Container):
        container.patient_repository().create(self.entity)