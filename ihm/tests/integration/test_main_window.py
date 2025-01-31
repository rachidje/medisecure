import pytest
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

from ihm.gui.views.create_patient_folder_view import CreatePatientFolderView
from ihm.core.medisecure_main_window import MedisecureMainWindow

@pytest.fixture
def app():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    yield app
    app.quit()

@pytest.fixture
def window():
    main_window = QMainWindow()
    ui = MedisecureMainWindow()
    ui.setupUi(main_window)
    return main_window

@pytest.mark.gui
class TestCreateFolderPatientGui:
    def test_display_create_patient_folder_view_when_menu_action_is_clicked(self,app, window: QMainWindow):
        """
        Teste que cliquer sur 'Create Patient Folder' affiche le widget CreatePatientFolderView.
        """
        with app:
            # Simuler l'affichage de la fenêtre principale
            window.show()

            # Trouver l'action 'Create Patient Folder'
            action_create_patient_folder = None
            for action in window.menuBar().actions(): # type: ignore
                if action.menu():
                    for sub_action in action.menu().actions(): # type: ignore
                        if sub_action.text() == "Create Patient Folder":
                            action_create_patient_folder = sub_action
                            break

            assert action_create_patient_folder is not None

            # Simuler un clic sur l'action du menu
            action_create_patient_folder.trigger()

            # Vérifier que le widget central est une instance de CreatePatientFolderView
            central_widget = window.centralWidget()
            assert isinstance(central_widget, QWidget), "Le widget central doit être un QWidget."
            assert isinstance(central_widget, CreatePatientFolderView), (
                "Le widget central n'est pas une instance de CreatePatientFolderView."
            )