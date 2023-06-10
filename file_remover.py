import logging

from PySide6.QtCore import Signal
from send2trash import send2trash

from interruptible_class import InterruptibleClass


class FileRemover(InterruptibleClass):
    file_removed = Signal(str)

    def __init__(self):
        # QObject.__init__(self)
        InterruptibleClass.__init__(self, parent=self)

    def remove_files(self, files):
        if logging.getLogger().isEnabledFor(logging.DEBUG):
            logging.debug(f"Removing files: {files}")
        else:
            logging.info("Removing files")
        for file in files:
            if self.need_to_interrupt():
                return
            try:
                send2trash(file)
                logging.debug(f"File removed: {file}")
            except Exception as e:
                logging.error(f"Failed to remove file: {file}, Error: {e}")
            finally:
                self.file_removed.emit(file)

        if logging.getLogger().isEnabledFor(logging.DEBUG):
            logging.debug(f"Removing files {files} done")
        else:
            logging.info("Removing files done")
