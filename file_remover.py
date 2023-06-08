from PySide6.QtCore import QObject, Signal
from send2trash import send2trash

from interruptible_class import InterruptibleClass


class FileRemover(QObject, InterruptibleClass):
    file_removed = Signal(str)

    def __init__(self):
        QObject.__init__(self)
        InterruptibleClass.__init__(self, parent=self)

    def remove_files(self, files):
        for file in files:
            if self.need_to_interrupt():
                return
            try:
                send2trash(file)
            except Exception as e:
                print(e)
            finally:
                self.file_removed.emit(file)
