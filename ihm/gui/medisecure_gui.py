from PyQt6.QtWidgets import QMainWindow, QMessageBox
from dependency_injector.wiring import inject, Provide

from ihm.gui.base_app import Ui_MainWindow
from patient_management.infrastructure.adapter.primary.controllers.patient_controller import PatientController
from shared.container.container import Container
from shared.domain.entities.user import User
from shared.domain.enum.roles_enum import Role


class MedisecureApp(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) #type: ignore

        self.create_folder_btn.clicked.connect(self.on_create_folder) # type: ignore

    def on_create_folder(self):
        self.create_folder()

    @inject
    def create_folder(self, controller: PatientController = Provide[Container.patient_controller]):
        print(controller)
        firstname = self.firstname_input.text()
        lastname = self.lastname_input.text()
        email = self.email_input.text()
        date_of_birth = self.date_of_birth_input.date().toString("yyyy-MM-dd")
        consent = self.consent_checkbox.isChecked()
        guardian_consent = self.guardian_consent_checkbox.isChecked()

        id = controller.create({
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "date_of_birth": date_of_birth,
            "consent": consent,
            "guardian_consent": guardian_consent,
            "medical_professional": User(id="1", firstname="John", lastname="Doe", email="john.doe@example.com", password="qwerty", roles=[Role.DOCTOR])
        })

        QMessageBox.information(self, "Medisecure", f"Created folder with ID: {id}")