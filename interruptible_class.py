from threading import Event

from PySide6.QtCore import QTimer, QThreadPool, QCoreApplication

from interruptible_task import InterruptibleTask


class InterruptibleClass:
    def __init__(self, parent=None):
        self.__list_of_workers = []
        self.__interrupt_event = Event()
        self.__timer = QTimer(QCoreApplication.instance())
        self.__timer.timeout.connect(self._try_interrupt)
        self.__timer.setInterval(1000)
        self.__timer.start()
        self.__thread_pool = QThreadPool()

    def interrupt(self):
        self.__interrupt_event.set()

    def _try_interrupt(self):
        if self.__interrupt_event.is_set():
            for worker in self.__list_of_workers:
                worker.interrupt()
            self.__thread_pool.waitForDone()

    def _add_task(self, fn, *args, **kwargs):
        # print(fn, args, kwargs)  # will go to logging
        worker = InterruptibleTask(fn, *args, **kwargs)
        self.__list_of_workers.append(worker)
        self.__thread_pool.start(worker)

    def _wait_for_tasks_completion(self):
        self.__thread_pool.waitForDone()
        self.__list_of_workers.clear()

    def need_to_interrupt(self):
        return self.__interrupt_event.is_set()
