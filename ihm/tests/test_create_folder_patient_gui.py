from datetime import date
from unittest.mock import patch
import pytest
from PyQt6.QtWidgets import QApplication, QMessageBox

from ihm.tests.test_gui import TestGui
from patient_management.application.usecases.create_patient_folder_usecase import PatientDataPayload
from shared.tests.fixtures.seeds.user_seeds import E2eUsers


@pytest.mark.gui
class TestCreateFolderPatientGui:

    def setup_method(self):
        self.test_gui = TestGui()
        self.test_gui.setup()

        self.test_gui.load_fixtures([
            E2eUsers.doctor, 
        ])

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
        data: PatientDataPayload = {
            "firstname": "John",
            "lastname": "Doe",
            "email": "john.doe@example.com",
            "date_of_birth": date(1990, 1, 1),
            "consent": True,
            "guardian_consent": False,
            "medical_professional": E2eUsers.doctor.entity
        }


        with patch.object(QMessageBox, "information", return_value=None) as mock_info:
            self.test_gui.gui.firstname_input.setText(data["firstname"])
            self.test_gui.gui.lastname_input.setText(data["lastname"])
            self.test_gui.gui.email_input.setText(data["email"])
            self.test_gui.gui.date_of_birth_input.setDate(data["date_of_birth"])
            self.test_gui.gui.consent_checkbox.setChecked(data["consent"])

            self.test_gui.gui.create_folder()

            # Vérifier que la méthode QMessageBox.information a été appelée
            mock_info.assert_called_once()

            # Vérifier que le texte du message contient un ID valide
            called_args = mock_info.call_args[0]  # Récupère les arguments passés à la méthode
            message_text: str = called_args[2]  # Texte du message
            assert message_text.startswith("Created folder with ID: ")
            generated_id = message_text.split(": ")[1]  # Extraire l'ID
            assert isinstance(generated_id, str)  # Vérifier que l'ID est une chaîne