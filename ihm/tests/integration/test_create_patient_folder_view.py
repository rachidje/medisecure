import pytest
from PyQt6.QtWidgets import QApplication

from ihm.gui.views.create_patient_folder_view import CreatePatientFolderView


@pytest.mark.gui
class TestCreatePatientFolderView:
    def test_display_all_fields(self):
        app = QApplication([]) # Create an application instance
        create_patient_folder_view = CreatePatientFolderView()
        create_patient_folder_view.setupUi(create_patient_folder_view)

        assert hasattr(create_patient_folder_view, "firstname_input")
        assert hasattr(create_patient_folder_view, "lastname_input")
        assert hasattr(create_patient_folder_view, "email_input")
        assert hasattr(create_patient_folder_view, "date_of_birth_input")
        assert hasattr(create_patient_folder_view, "consent_checkbox")
        assert hasattr(create_patient_folder_view, "guardian_consent_checkbox")
        assert hasattr(create_patient_folder_view, 'create_folder_btn')
        assert hasattr(create_patient_folder_view, 'cancel_create_folder_btn')
