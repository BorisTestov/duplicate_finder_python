from PySide6.QtCore import QRunnable, Signal, Slot, QTimer, QObject


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
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.check_interrupt)
        self.isInterruptionRequested = False

    def interrupt(self):
        self.isInterruptionRequested = True

    def check_interrupt(self):
        if self.isInterruptionRequested:
            raise Exception("Interrupt requested")

    @Slot()
    def run(self):
        self.timer.start()
        self.started.emit()
        try:
            result = self.fn(*self.args, **self.kwargs)
            self.result.emit(result)
        except Exception as e:
            self.error.emit((e, "Task was interrupted"))
        else:
            self.timer.stop()
            self.timer.deleteLater()
            self.finished.emit()
