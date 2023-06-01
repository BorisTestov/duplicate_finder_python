from PySide6.QtWidgets import QMainWindow, QDialog

from ui.ui_confirmation_dialog import Ui_delete_files_dialog
from ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.progress_bar.setVisible(False)


class ConfirmationDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_delete_files_dialog()
        self.ui.setupUi(self)
