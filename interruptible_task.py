import logging

from PySide6.QtCore import QRunnable, Signal, Slot, QTimer, QObject, QEventLoop


class InterruptionError(Exception):
    pass


class InterruptibleTask(QRunnable, QObject):
    started = Signal()
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)

    def __init__(self, fn, *args, **kwargs):
        QRunnable.__init__(self)
        QObject.__init__(self)

        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.isInterruptionRequested = False

    def interrupt(self):
        self.isInterruptionRequested = True

    @Slot()
    def run(self):
        def check_interrupt():
            if self.isInterruptionRequested:
                logging.warning("Task interrupted")
                raise InterruptionError("Interrupt requested")

        event_loop = QEventLoop()
        timer = QTimer()
        timer.setInterval(1000)
        timer.timeout.connect(check_interrupt)
        timer.start()
        self.started.emit()

        try:
            result = self.fn(*self.args, **self.kwargs)
            self.result.emit(result)
        except InterruptionError as e:
            logging.error("Task error occurred", exc_info=True)
            logging.error(e)
        except Exception as e:
            logging.error("Task error occurred", exc_info=True)
            logging.error(e)
            self.error.emit((e, "Error occured"))
            raise
        else:
            logging.debug("Task finished successfully")
        finally:
            timer.stop()
            timer.deleteLater()
            self.finished.emit()

            event_loop.exit()
