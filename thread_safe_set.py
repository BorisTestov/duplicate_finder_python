from __future__ import annotations

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

    def __eq__(self, other: ThreadSafeSet):
        with self.lock:
            with other.lock:
                return self.set == other.set

    def __repr__(self):
        with self.lock:
            return self.set.__repr__()
