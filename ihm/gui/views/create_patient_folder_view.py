from datetime import date
from PyQt6.QtWidgets import QWidget, QMessageBox
from dependency_injector.wiring import inject, Provide

from ihm.gui.generated.base_create_patient_folder_view import Ui_Form
from patient_management.infrastructure.adapter.primary.controllers.patient_controller import PatientController
from shared.container.container import Container
from shared.tests.fixtures.seeds.user_seeds import E2eUsers


class CreatePatientFolderView(QWidget, Ui_Form):
    def setupUi(self, Form: QWidget):
        super().setupUi(Form)

        if not self.are_all_fields_filled():
            self.create_folder_btn.setEnabled(False)

        if self.firstname_input:
            self.firstname_input.textChanged.connect(self.update_create_folder_btn_state)
        if self.lastname_input:
            self.lastname_input.textChanged.connect(self.update_create_folder_btn_state)
        if self.email_input:
            self.email_input.textChanged.connect(self.update_create_folder_btn_state)

        self.create_folder_btn.clicked.connect(lambda: self.create_folder())

    @inject
    def create_folder(self, controller: PatientController = Provide[Container.patient_controller]):
        try:
            id =controller.create({
                "firstname": self.firstname_input.text(),
                "lastname": self.lastname_input.text(),
                "email": self.email_input.text(),
                "date_of_birth": date.fromisoformat(self.date_of_birth_input.date().toString("yyyy-MM-dd")),
                "consent": self.consent_checkbox.isChecked(),
                "guardian_consent": self.guardian_consent_checkbox.isChecked(),
                "medical_professional": E2eUsers.doctor.entity
            })
            QMessageBox.information(self, "Medisecure", f"Created folder with ID: {id}")
        except Exception as e:
            QMessageBox.warning(self, "Medisecure - Error", str(e))


    def update_create_folder_btn_state(self):
        self.create_folder_btn.setEnabled(self.are_all_fields_filled())

    def are_all_fields_filled(self):
        fields = [
            self.firstname_input,
            self.lastname_input,
            self.email_input,
        ]
        return all(field.text() != "" for field in fields)
    
