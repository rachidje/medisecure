from PyQt6.QtWidgets import QWidget
from ihm.gui.generated.base_create_patient_folder_view import Ui_Form


class CreatePatientFolderView(QWidget, Ui_Form):
    def setupUi(self, Form: QWidget):
        super().setupUi(Form)