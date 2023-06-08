from PySide6.QtCore import QTimer, QCoreApplication


def check_by_timer(func):
    def wrapper(*args, **kwargs):
        timer = QTimer()
        timer.moveToThread(QCoreApplication.instance().thread())
        timer.timeout.connect(args[0].on_interrupt)
        timer.start(1000)
        result = func(*args, **kwargs)
        timer.stop()
        return result

    return wrapper
