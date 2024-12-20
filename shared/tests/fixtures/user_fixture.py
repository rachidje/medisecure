from shared.domain.entities.user import User
from shared.tests.fixtures.fixture_protocol import FixtureProtocol
from dependency_injector.wiring import Container

class UserFixture(FixtureProtocol):
    def __init__(self, entity: User):
        self.entity = entity

    def load(self, container: Container):
        container.user_repository().create(self.entity)