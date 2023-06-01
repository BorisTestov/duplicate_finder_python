# from version import APP_VERSION, BUILD_NUMBER

import sys

from PySide6.QtWidgets import QApplication

from ui.gui import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
