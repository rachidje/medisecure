from datetime import date
from unittest.mock import patch
import pytest
from PyQt6.QtWidgets import QApplication, QMessageBox

from ihm.tests.test_gui import TestGui
from shared.tests.fixtures.seeds.user_seeds import E2eUsers


@pytest.mark.gui
class TestCreateFolderPatientGui:

    def setup_method(self):
        self.test_gui = TestGui()
        self.test_gui.setup()

        self.test_gui.load_fixtures([
            E2eUsers.doctor, 
        ])

    def fill_form(self):
        self.test_gui.gui.firstname_input.setText("John")
        self.test_gui.gui.lastname_input.setText("Doe")
        self.test_gui.gui.email_input.setText("john.doe@example.com")
        self.test_gui.gui.date_of_birth_input.setDate(date(1990, 1, 1))
        self.test_gui.gui.consent_checkbox.setChecked(True)
        self.test_gui.gui.guardian_consent_checkbox.setChecked(False)

    def test_create_folder_tab_initialization(self, qapp: QApplication):
        assert self.test_gui.gui.windowTitle() == "Medisecure"
        assert self.test_gui.gui.tabWidget.currentIndex() == 0

        assert self.test_gui.gui is not None
        assert hasattr(self.test_gui.gui, "firstname_input")
        assert hasattr(self.test_gui.gui, "lastname_input")
        assert hasattr(self.test_gui.gui, "email_input")
        assert hasattr(self.test_gui.gui, "date_of_birth_input")
        assert hasattr(self.test_gui.gui, "consent_checkbox")
        assert hasattr(self.test_gui.gui, "guardian_consent_checkbox")
        assert hasattr(self.test_gui.gui, 'create_folder_btn')
        assert hasattr(self.test_gui.gui, 'cancel_create_folder_btn')

    def test_display_message_box_with_ID_generated(self):
        self.fill_form()

        with patch.object(QMessageBox, "information", return_value=None) as mock_info:
            self.test_gui.gui.create_folder()

            mock_info.assert_called_once()

            called_args = mock_info.call_args[0]  # Récupère les arguments passés à la méthode
            message_text: str = called_args[2]  # Texte du message
            assert message_text.startswith("Created folder with ID: ")
            generated_id = message_text.split(": ")[1]  # Extraire l'ID
            assert isinstance(generated_id, str)  # Vérifier que l'ID est une chaîne

    def test_should_display_warning_box_if_consent_patient_is_not_checked(self):
        self.fill_form()
        self.test_gui.gui.consent_checkbox.setChecked(False)

        with patch.object(QMessageBox, "warning", return_value=None) as mock_warning:
            self.test_gui.gui.create_folder()

            mock_warning.assert_called_once()
            called_args = mock_warning.call_args[0]  # Récupère les arguments passés à la méthode
            
            assert "Unable to create folder without consent patient" in called_args[2]  # Texte du message

    def test_should_display_warning_box_if_all_fields_are_empty(self):
        self.fill_form()
        self.test_gui.gui.firstname_input.setText("")
        self.test_gui.gui.lastname_input.setText("")
        self.test_gui.gui.email_input.setText("")

        with patch.object(QMessageBox, "warning", return_value=None) as mock_warning:
            self.test_gui.gui.create_folder()

            mock_warning.assert_called_once()
            called_args = mock_warning.call_args[0]  # Récupère les arguments passés à la méthode
            
            assert "Please fill all fields" in called_args[2]  # Texte du message

