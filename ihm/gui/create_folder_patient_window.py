from ihm.gui.create_folder_patient_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow


class CreateFolderPatientWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) #type: ignore