import sys

from PySide6.QtWidgets import QApplication

from ui.mainwindow import MainWindow
from version import APP_VERSION, BUILD_NUMBER


def main():
    print(f"version: {APP_VERSION} build: {BUILD_NUMBER}")
    app = QApplication(sys.argv)
    window = MainWindow()
    app.aboutToQuit.connect(window.searcher.abort)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

# TODO add usage instructions to README
# TODO add logging to logfiles
