import logging
from collections import deque

from PySide6.QtCore import QObject, Signal

from searcher import Searcher


class CLIRunner(QObject):
    searcher = Searcher()

    finished = Signal()

    def __init__(self, remove_after_find=False):
        QObject.__init__(self)
        self.searcher.search_done.connect(self.print_output)
        self.searcher.all_files_added.connect(self.searcher.find)
        if remove_after_find:
            self.searcher.search_done.connect(lambda d: self.searcher.remove(deque(set(value) for value in d.values())))
            self.searcher.all_files_removed.connect(lambda: self.finished.emit())
        else:
            self.searcher.search_done.connect(lambda: self.finished.emit())

    def print_output(self, result):
        output = "\n\nDUPLICATES:\n"
        for key, value in result.items():
            output += f"{key}"
            for v in value:
                output += f"\t{v}"
        output += "\n\n"
        logging.info(output)

    def run(self, include_directories, exclude_directories, include_masks, exclude_masks, depth, min_file_size,
            search_type):
        self.searcher.scan(include_directories, exclude_directories, include_masks, exclude_masks, depth, min_file_size,
                           search_type)

    def abort(self):
        self.searcher.interrupt()
