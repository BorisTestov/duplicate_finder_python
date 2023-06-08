from __future__ import annotations

import threading


class ThreadSafeDict:
    def __init__(self, *args, **kwargs):
        self.lock = threading.Lock()
        self.dict = dict(*args, **kwargs)

    def __repr__(self):
        with self.lock:
            return self.dict.__repr__()

    def __getitem__(self, key):
        with self.lock:
            return self.dict[key]

    def __setitem__(self, key, value):
        with self.lock:
            self.dict[key] = value

    def __delitem__(self, key):
        with self.lock:
            del self.dict[key]

    def __contains__(self, key):
        with self.lock:
            return key in self.dict

    def __iter__(self):
        with self.lock:
            return iter(self.dict.copy())

    def __len__(self):
        with self.lock:
            return len(self.dict)

    def __eq__(self, other: ThreadSafeDict):
        with self.lock:
            with other.lock:
                return self.dict == other.dict

    def items(self):
        with self.lock:
            return self.dict.items()

    def keys(self):
        with self.lock:
            return self.dict.keys()

    def values(self):
        with self.lock:
            return self.dict.values()

    def clear(self):
        with self.lock:
            self.dict.clear()
