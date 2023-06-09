import logging
from collections import deque
from typing import Set

from PySide6.QtCore import Signal

from directory_scanner import DirectoryScanner
from duplicates_finder import DuplicatesFinder
from file_remover import FileRemover
from interruptible_class import InterruptibleClass


class Searcher(InterruptibleClass):
    dir_scanner = DirectoryScanner()
    finder = DuplicatesFinder()
    remover = FileRemover()

    all_files_added = Signal(deque)
    search_done = Signal(dict)
    file_scanned = Signal()
    file_removed = Signal(str)
    all_files_removed = Signal()
    scanning_started = Signal()
    removing_started = Signal()
    dir_scanner_interrupted = Signal()
    file_remover_interrupted = Signal()
    finder_interrupted = Signal()

    def __init__(self):
        # QObject.__init__(self)
        InterruptibleClass.__init__(self, parent=self)
        self.search_type = None

        self.dir_scanner.all_files_added.connect(self.all_files_added)
        self.finder.search_done.connect(self.search_done)
        self.finder.file_scanned.connect(self.file_scanned)
        self.remover.file_removed.connect(self.file_removed)
        self.dir_scanner.interrupted.connect(self.dir_scanner_interrupted)
        self.finder.interrupted.connect(self.finder_interrupted)
        self.remover.interrupted.connect(self.file_remover_interrupted)

    def scan(self, include_directories, exclude_directories, include_masks, exclude_masks, depth, min_file_size,
             search_type):
        self.scanning_started.emit()
        logging.debug(
            f"Started scanning with parameters: "
            f"{include_directories=} {exclude_directories=} "
            f"{include_masks=} {exclude_masks=} "
            f"{depth=} {min_file_size=} {search_type=}")
        self.dir_scanner.depth = depth
        self.dir_scanner.min_file_size = min_file_size
        self.dir_scanner.include_directories = include_directories
        self.dir_scanner.exclude_directories = exclude_directories
        self.dir_scanner.include_masks = include_masks
        self.dir_scanner.exclude_masks = exclude_masks
        self.search_type = search_type
        self._add_task(self.dir_scanner.scan)
        self._wait_for_tasks_completion()

    def find(self, files):
        self._add_task(self.finder.find_duplicates, files, self.search_type)
        self._wait_for_tasks_completion()

    def remove(self, files_matrix: deque[Set[str]]):
        self.removing_started.emit()
        self._add_task(self.__remove_handler, files_matrix)
        self._wait_for_tasks_completion()
        self.all_files_removed.emit()

    def __remove_handler(self, files_matrix: deque[Set[str]]):
        for files in files_matrix:
            self._add_task(self.remover.remove_files, files)

    def abort(self):
        logging.debug("Interrupting...")
        self.dir_scanner.interrupt()
        self.finder.interrupt()
        self.remover.interrupt()
        self.interrupt()
