import threading


class ThreadSafeSet:
    def __init__(self, iterable=None):
        self.set = set(iterable) if iterable is not None else set()
        self.lock = threading.Lock()

    def add(self, item):
        with self.lock:
            self.set.add(item)

    def remove(self, item):
        with self.lock:
            self.set.remove(item)

    def clear(self):
        with self.lock:
            self.set.clear()

    def __contains__(self, item):
        with self.lock:
            return item in self.set

    def __iter__(self):
        with self.lock:
            return iter(self.set.copy())

    def __len__(self):
        with self.lock:
            return len(self.set)
