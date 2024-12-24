import sys
import pytest
from PyQt6.QtWidgets import QApplication, QMainWindow

from ihm.gui.create_folder_patient_window import CreateFolderPatientWindow


@pytest.fixture
def app():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    yield app
    app.quit()

@pytest.mark.gui
class TestCreateFolderPatientGui:

    def test_create_folder_window_initialization(self, qapp: QApplication):
        window: QMainWindow = CreateFolderPatientWindow()
        assert window.windowTitle() == "Create folder patient"

        assert window is not None
        assert hasattr(window, "firstname_input")
        assert hasattr(window, "lastname_input")
        assert hasattr(window, "email_input")
        assert hasattr(window, "date_of_birth_input")
        assert hasattr(window, "consent_checkbox")
        assert hasattr(window, "guardian_consent_checkbox")
        assert hasattr(window, 'create_folder_btn')
        assert hasattr(window, 'cancel_create_folder_btn')