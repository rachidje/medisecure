import pytest
from PyQt6.QtWidgets import QApplication

from ihm.gui.views.create_patient_folder_view import CreatePatientFolderView

@pytest.fixture
def app():
    app = QApplication([])
    yield app
    app.quit()

@pytest.fixture
def create_patient_folder_view(app):
    view = CreatePatientFolderView()
    view.setupUi(view)
    return view
    

@pytest.mark.gui
class TestCreatePatientFolderView:
    def test_display_all_fields(self, create_patient_folder_view: CreatePatientFolderView):
        assert hasattr(create_patient_folder_view, "firstname_input")
        assert hasattr(create_patient_folder_view, "lastname_input")
        assert hasattr(create_patient_folder_view, "email_input")
        assert hasattr(create_patient_folder_view, "date_of_birth_input")
        assert hasattr(create_patient_folder_view, "consent_checkbox")
        assert hasattr(create_patient_folder_view, "guardian_consent_checkbox")
        assert hasattr(create_patient_folder_view, 'create_folder_btn')
        assert hasattr(create_patient_folder_view, 'cancel_create_folder_btn')

    def test_create_folder_btn_is_disabled_when_all_fields_are_empty(self, create_patient_folder_view: CreatePatientFolderView):
        create_patient_folder_view.firstname_input.setText("")
        create_patient_folder_view.lastname_input.setText("")
        create_patient_folder_view.email_input.setText("")

        assert create_patient_folder_view.create_folder_btn.isEnabled() == False

    def test_create_folder_btn_is_enabled_when_all_fields_are_not_empty(self, create_patient_folder_view: CreatePatientFolderView):
        create_patient_folder_view.firstname_input.setText("John")
        assert create_patient_folder_view.create_folder_btn.isEnabled() == False

        create_patient_folder_view.lastname_input.setText("Doe")
        assert create_patient_folder_view.create_folder_btn.isEnabled() == False

        create_patient_folder_view.email_input.setText("john.doe@example.com")
        assert create_patient_folder_view.create_folder_btn.isEnabled() == True