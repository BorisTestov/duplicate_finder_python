import sys

from PySide6.QtWidgets import QApplication

from ui.mainwindow import MainWindow
from version import APP_VERSION, BUILD_NUMBER

if __name__ == "__main__":
    print(f"version: {APP_VERSION} build: {BUILD_NUMBER}")
    app = QApplication(sys.argv)
    window = MainWindow()
    app.aboutToQuit.connect(window.searcher.abort)
    window.show()
    sys.exit(app.exec())
    
    # TODO fix tests
    # TODO fix types hint, probably generate docs
