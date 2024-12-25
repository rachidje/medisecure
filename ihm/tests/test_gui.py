from PyQt6.QtWidgets import QApplication
from sqlalchemy.orm import Session
import sys

from ihm.gui.medisecure_gui import MedisecureApp
from patient_management.domain.entities.patient_model import PatientModel
from shared.adapters.secondary.mysql_db.connection import get_session
from shared.container.container import Container
from shared.domain.models.user_model import UserModel
from shared.tests.fixtures.fixture_protocol import FixtureProtocol


class TestGui:
    _app: QApplication
    _gui: MedisecureApp
    _container: Container
    _session: Session

    def setup(self):
        self._container = Container()
        self._session = get_session()

        if QApplication.instance() is None:
            self._app = QApplication(sys.argv)

        self._session.query(PatientModel).delete()
        self._session.query(UserModel).delete()
        self._session.commit()

        self._container.wire(modules=[
            "ihm.gui.medisecure_gui"
        ])

        self._gui = MedisecureApp()

    def load_fixtures(self, fixtures: list[FixtureProtocol]):
        for fixture in fixtures:
            fixture.load(self.container)

    @property
    def gui(self):
        return self._gui
    
    @property
    def container(self):
        return self._container