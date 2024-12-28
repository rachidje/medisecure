from datetime import date
from unittest.mock import patch
import pytest
from PyQt6.QtWidgets import QApplication, QMessageBox

from ihm.gui.views.create_patient_folder_view import CreatePatientFolderView
from ihm.tests.utils.test_gui import TestGui



@pytest.mark.gui
class TestCreatePatientFolderView:
    _test_gui = TestGui
    _view: CreatePatientFolderView

    def setup_method(self):
        self._test_gui = TestGui()
        self._test_gui.setup()
        self._view = self._test_gui.initialize_view(CreatePatientFolderView)

    def teardown_method(self):
        self._test_gui.teardown()

    def test_display_all_needed_fields(self):
        assert hasattr(self._view, "firstname_input")
        assert hasattr(self._view, "lastname_input")
        assert hasattr(self._view, "email_input")
        assert hasattr(self._view, "date_of_birth_input")
        assert hasattr(self._view, "consent_checkbox")
        assert hasattr(self._view, "guardian_consent_checkbox")
        assert hasattr(self._view, 'create_folder_btn')
        assert hasattr(self._view, 'cancel_create_folder_btn')

    def test_create_folder_btn_is_disabled_when_all_fields_are_empty(self):
        self._view.firstname_input.setText("")
        self._view.lastname_input.setText("")
        self._view.email_input.setText("")

        assert self._view.create_folder_btn.isEnabled() == False

    def test_create_folder_btn_is_enabled_when_all_fields_are_fully_filled(self):
        self._view.firstname_input.setText("John")
        assert self._view.create_folder_btn.isEnabled() == False

        self._view.lastname_input.setText("Doe")
        assert self._view.create_folder_btn.isEnabled() == False

        self._view.email_input.setText("john.doe@example.com")
        assert self._view.create_folder_btn.isEnabled() == True

    def test_should_display_warning_box_if_any_domain_validation_fails(self):
        self._view.firstname_input.setText("John")
        self._view.lastname_input.setText("Doe")
        self._view.email_input.setText("john.doe@example.com")
        self._view.date_of_birth_input.setDate(date(1990, 1, 1))
        self._view.consent_checkbox.setChecked(False)
        self._view.guardian_consent_checkbox.setChecked(False)

        with patch.object(QMessageBox, "warning", return_value=None) as mock_warning:
            self._view.create_folder()

            mock_warning.assert_called_once()
            called_args = mock_warning.call_args[0]  # Récupère les arguments passés à la méthode
            
            assert "Unable to create folder without consent patient" in called_args[2]  # Texte du message