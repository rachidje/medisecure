from PyQt6.QtWidgets import QWidget

from ihm.gui.generated.base_create_patient_folder_view import Ui_Form


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

    def update_create_folder_btn_state(self):
        self.create_folder_btn.setEnabled(self.are_all_fields_filled())

    def are_all_fields_filled(self):
        fields = [
            self.firstname_input,
            self.lastname_input,
            self.email_input,
        ]
        return all(field.text() != "" for field in fields)
    
