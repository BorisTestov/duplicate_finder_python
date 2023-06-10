import argparse
import logging
import logging.handlers
import os
import signal
import sys

from PySide6.QtCore import QTranslator, QLocale, QSettings, QCoreApplication
from PySide6.QtWidgets import QApplication

from cli_runner import CLIRunner
from ui.mainwindow import MainWindow
from ui.mappings import Mappings
from version import APP_VERSION, BUILD_NUMBER


def parse_arguments():
    parser = argparse.ArgumentParser(description='Directory Scanner')

    parser.add_argument('--cli', action='store_true',
                        help='Indicates that the app will run from console')

    parser.add_argument("-v", "--version", action="store_true", help="Print the application version and exit")

    parser.add_argument("--loglevel", choices=["debug", "info", "warning", "error", "critical"], default="info",
                        help="Set the logging level (default: info)")

    if '--cli' in sys.argv:
        parser.add_argument('--include-directories', nargs='+', required=True,
                            help='Array of directories to include')

        parser.add_argument('--exclude-directories', nargs='+', default=[],
                            help='Array of directories to exclude')

        parser.add_argument('--include-masks', nargs='+', default=[],
                            help='Array of masks to include')

        parser.add_argument('--exclude-masks', nargs='+', default=[],
                            help='Array of masks to exclude')

        parser.add_argument('--min-file-size-bytes', type=int, default=0,
                            help='Minimum file size in bytes')

        parser.add_argument('--depth', type=int, default=0,
                            help='Depth of directory scanning')

        parser.add_argument('--search-type', type=str, default='hash',
                            help='Type of search to perform')

        parser.add_argument('--remove-after-find', action='store_true', default=False,
                            help='Removes the file after it is found')

    try:
        args = parser.parse_args()
        if hasattr(args, 'include_directories') and args.include_directories is not None:
            if not args.include_directories:
                parser.error("--include-directories requires at least one directory.")
        return args
    except (argparse.ArgumentError, argparse.ArgumentTypeError) as e:
        print(str(e), file=sys.stderr)
        parser.print_help(sys.stderr)
    except Exception as e:
        print(str(e), file=sys.stderr)
        parser.print_help(sys.stderr)
    sys.exit(1)


def handle_gui_run():
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


def handle_cli_run(args):
    app = QCoreApplication(sys.argv)

    runner = CLIRunner(args.remove_after_find)
    app.aboutToQuit.connect(runner.searcher.abort)
    runner.finished.connect(app.quit)

    runner.run(
        args.include_directories,
        args.exclude_directories,
        args.include_masks,
        args.exclude_masks,
        args.depth,
        args.min_file_size_bytes,
        Mappings.type_mappings[args.search_type]
    )
    app.exec()
    sys.exit(0)


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    # print(sys.stdout)
    # print(sys.__stdout__)

    if hasattr(sys, '_MEIPASS'):
        os.chdir(sys._MEIPASS)
    args = parse_arguments()
    # print(args.cli)
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

    if os.path.isfile(log_file):
        rotate_number = 1
        while os.path.isfile(f"{log_file}.{rotate_number}"):
            rotate_number += 1

        if rotate_number > 5:
            os.remove(f"{log_file}.{rotate_number - 1}")
            rotate_number -= 1

        for i in range(rotate_number, 0, -1):
            os.rename(f"{log_file}.{i - 1 if i > 1 else ''}", f"{log_file}.{i}")

    rotating_handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5)
    rotating_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s %(threadName)s] %(levelname)s: %(message)s')
    rotating_handler.setFormatter(formatter)
    logging.basicConfig(level=args.loglevel.upper(), handlers=[rotating_handler, logging.StreamHandler(sys.stdout)])

    logging.info(f"version: {APP_VERSION} build: {BUILD_NUMBER}")

    if not args.cli:
        logging.info('Running with GUI option')
        handle_gui_run()
    else:
        logging.info('Running with CLI option')
        handle_cli_run(args)


if __name__ == "__main__":
    main()
