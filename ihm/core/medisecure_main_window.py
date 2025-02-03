from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6.QtCore import QObject

from ihm.gui.generated.base_app import Ui_MainWindow
from ihm.gui.views.create_patient_folder_view import CreatePatientFolderView


class MedisecureMainWindow(Ui_MainWindow):
    def setupUi(self, MainWindow: QMainWindow):
        super().setupUi(MainWindow)

        self.actionCreate_Patient_Folder.triggered.connect(
            lambda: self.change_central_widget(MainWindow,CreatePatientFolderView())
        )

    def change_central_widget(self, MainWindow: QMainWindow, widget: CreatePatientFolderView):
        """
        Change dynamiquement le widget central.
        """
        widget.setupUi(widget)
        MainWindow.setCentralWidget(widget)
