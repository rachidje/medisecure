from shared.container.container import Container
from shared.domain.entities.user import User
from shared.tests.fixtures.fixture_protocol import FixtureProtocol

class UserFixture(FixtureProtocol):
    def __init__(self, entity: User):
        self.entity = entity

    def load(self, container: Container):
        container.user_repository().create(self.entity)