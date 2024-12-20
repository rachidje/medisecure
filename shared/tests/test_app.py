from fastapi import FastAPI

from api.handlers.exception_handlers import unauthorized_exception_handler
from api.routers import patient_router
from patient_management.domain.entities.patient_model import PatientModel
from shared.adapters.secondary.mysql_db.connection import get_session
from shared.container.container import Container
from shared.domain.models.user_model import UserModel
from shared.exceptions.user.unauthorized_role_exception import UnauthorizedRoleException
from shared.tests.fixtures.fixture_protocol import FixtureProtocol


class TestApp:
    _app = FastAPI()
    _container = Container()
    _session = get_session()

    def setup(self):
        self._session.query(PatientModel).delete()
        self._session.query(UserModel).delete()
        self._session.commit()

        self._container.wire(modules=[
            "api.routers.patient_router",
            "api.middlewares.authentication_middleware",
        ])

        self._app.add_exception_handler(UnauthorizedRoleException, unauthorized_exception_handler)
        self._app.include_router(patient_router.router)

    def load_fixtures(self, fixtures: list[FixtureProtocol]):
        for fixture in fixtures:
            fixture.load(self.container)

    @property
    def app(self):
        return self._app
    
    @property
    def container(self):
        return self._container