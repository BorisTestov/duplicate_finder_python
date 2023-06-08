import os
import traceback
from collections import defaultdict
from typing import Set

from PySide6.QtCore import Signal, QObject, QThreadPool

from factories import TrieSplitMethodFactory, FileGrouperFactory
from hashed_file import HashedFile
from interruptible_class import InterruptibleClass
from search_types import SearchTypes
from thread_safe_dict import ThreadSafeDict
from trie import Trie


class DuplicatesFinder(QObject, InterruptibleClass):
    search_done = Signal(dict)
    file_scanned = Signal()

    def __init__(self):
        QObject.__init__(self)
        InterruptibleClass.__init__(self, parent=self)
        self.__factory = TrieSplitMethodFactory()
        self.__duplicates = ThreadSafeDict()
        self.__thread_pool = QThreadPool()

    def find_duplicates(self, files_to_scan, search_type: SearchTypes):
        self.__duplicates.clear()
        groupped_files = self.__group_files(files_to_scan, search_type)
        for files in groupped_files.values():
            self._add_task(self.__find_group_duplicates, files, search_type)
        self._wait_for_tasks_completion()
        self.search_done.emit(self.__duplicates.dict)

    def __group_files(self, files, search_type: SearchTypes):
        grouping_method = FileGrouperFactory[search_type]
        groupped_files = defaultdict(set)
        for file in files:
            if self.need_to_interrupt():
                return
            key = grouping_method(file)
            groupped_files[key].add(file)
        return groupped_files

    def __find_group_duplicates(self, files: Set, search_type: SearchTypes):
        if self.need_to_interrupt():
            return
        if len(files) < 2:
            return []
        trie = Trie(self.__factory[search_type])
        for path in files:
            try:
                if self.need_to_interrupt():
                    return
                if os.access(path, os.R_OK):
                    with HashedFile(path) as hfile:
                        trie.add_file(hfile)
            except Exception as e:
                traceback.print_exc(limit=None, file=None, chain=True)
                print(e)
        for duplicates in trie.find_duplicates():
            if self.need_to_interrupt():
                return
            min_file = min(duplicates)
            duplicates.remove(min_file)
            self.__duplicates[min_file] = duplicates

    def __find_duplicates_task(self, files_to_scan, search_type: SearchTypes):
        groupped_files = self.__group_files(files_to_scan, search_type)
        for files in groupped_files.values():
            self._add_task(self.__find_group_duplicates, files, search_type)
        self._wait_for_tasks_completion()
