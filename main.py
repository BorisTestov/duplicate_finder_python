import argparse
import logging
import logging.handlers
import os
import sys

from PySide6.QtCore import QTranslator, QLocale, QSettings
from PySide6.QtWidgets import QApplication

from ui.mainwindow import MainWindow
from version import APP_VERSION, BUILD_NUMBER


def main():
    try:
        os.chdir(sys._MEIPASS)
    except AttributeError:
        pass
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", action="store_true", help="Print the application version and exit")
    parser.add_argument("--loglevel", choices=["debug", "info", "warning", "error", "critical"], default="info",
                        help="Set the logging level (default: info)")
    args = parser.parse_args()

    print(f"Version: {APP_VERSION} Build: {BUILD_NUMBER}")
    if args.version:
        print(f"Version: {APP_VERSION}")
        print(f"Build: {BUILD_NUMBER}")
        return

    if sys.platform == "win32":
        default_log_dir = os.getenv("APPDATA")
        log_dir = os.path.join(default_log_dir, "DuplicateFinder", "logs")
    else:
        default_log_dir = os.path.expanduser("~")
        log_dir = os.path.join(default_log_dir, ".DuplicateFinder", "logs")

    print(f"Logs stored in {log_dir}")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "application.log")
    logging.basicConfig(level=args.loglevel.upper(),
                        format="[%(asctime)s %(threadName)s] %(levelname)s: %(message)s",
                        handlers=[
                            logging.handlers.RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5),
                            logging.StreamHandler(sys.stdout)
                        ])

    logging.info(f"version: {APP_VERSION} build: {BUILD_NUMBER}")

    app = QApplication(sys.argv)
    settings = QSettings("BTestov", "DuplicateFinder")
    locale = settings.value("locale", QLocale.system().name())

    def load_translators(locale):
        translator_main = QTranslator()
        translator_dialog = QTranslator()

        if translator_main.load(f"main_{locale}", "translations"):
            app.installTranslator(translator_main)
        else:
            logging.error(f"Unable to load main locale {locale}")

        if translator_dialog.load(f"dialog_{locale}", "translations"):
            app.installTranslator(translator_dialog)
        else:
            logging.error(f"Unable to load dialog locale {locale}")

        return translator_main, translator_dialog

    translators = load_translators(locale)

    def update_locale(locale):
        nonlocal translators
        translators = load_translators(locale)
        settings.setValue("locale", locale)

    window = MainWindow()
    app.aboutToQuit.connect(window.searcher.abort)
    window.languageChanged.connect(update_locale)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
