import sys
from pathlib import Path

# Ajouter le répertoire racine au sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))


from PyQt6.QtWidgets import QApplication, QMainWindow
from ihm.gui.medisecure_gui import MedisecureApp
from shared.container.container import Container

if __name__ == "__main__":
    container = Container()

    container.wire(
        modules=[
            "ihm.gui.medisecure_gui"
        ]
    )

    app = QApplication(sys.argv)
    gui = MedisecureApp()

    gui.show()
    sys.exit(app.exec())