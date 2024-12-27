from PyQt6.QtWidgets import QApplication, QMainWindow
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))

from ihm.core.medisecure_main_window import MedisecureMainWindow

if __name__ == "__main__":
    
    app = QApplication([])
    main_window = QMainWindow()
    ui = MedisecureMainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec())