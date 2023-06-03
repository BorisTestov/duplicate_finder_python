from PySide6.QtWidgets import QDialog

from ui.ui_confirmation_dialog import Ui_delete_files_dialog


class ConfirmationDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_delete_files_dialog()
        self.ui.setupUi(self)
        self.__connect_slots()

    def __connect_slots(self):
        self.ui.delete_files_cancel_button.clicked.connect(self.reject)
        self.ui.delete_files_ok_button.clicked.connect(self.accept)
