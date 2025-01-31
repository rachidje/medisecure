from PyQt6.QtWidgets import QApplication, QMainWindow
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))

from ihm.gui.views.connection_view import ConnectionView
from shared.container.container import Container
from ihm.core.medisecure_main_window import MedisecureMainWindow

if __name__ == "__main__":
    
    app = QApplication([])

    main_window = QMainWindow()
    ui = MedisecureMainWindow()
    ui.setupUi(main_window)
    main_window.show()

    containe = Container()
    containe.wire(modules=[
        "ihm.core.medisecure_main_window",
        "ihm.gui.views.create_patient_folder_view",
    ])

    sys.exit(app.exec())