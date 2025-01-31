from ihm.gui.generated.connection_dialog_base import Ui_ConnectionDialog
from PyQt6.QtWidgets import QDialog


class ConnectionView(QDialog,Ui_ConnectionDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)