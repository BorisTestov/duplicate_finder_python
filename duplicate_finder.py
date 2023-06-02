import os
import re
from collections import defaultdict
from typing import Set, Union

from PySide6.QtCore import QCryptographicHash, QThreadPool, QMutex, QMutexLocker
from typeguard import typechecked

from hashed_file import HashedFile
from search_types import SearchTypes
from worker import Worker


class DuplicateFinder:
    @typechecked
    def __init__(self,
                 search_type: SearchTypes = SearchTypes.BY_HASH,
                 hash_method: QCryptographicHash.Algorithm = QCryptographicHash.Algorithm.Md5,
                 depth: int = 0,
                 min_file_size: int = 0,
                 blocksize: int = 512,
                 include_directories: Union[Set[os.path], None] = None,
                 exclude_directories: Union[Set[os.path], None] = None,
                 include_masks: Union[Set[str], None] = None,
                 exclude_masks: Union[Set[str], None] = None):
        if include_directories is None:
            raise ValueError("You must set include directories to check")
        include_directories = set(dir for dir in include_directories if os.path.exists(dir) and os.path.isdir(dir))
        if exclude_directories is not None:
            exclude_directories = set(dir for dir in exclude_directories if os.path.exists(dir) and os.path.isdir(dir))
            include_directories -= exclude_directories

        if include_masks is not None and exclude_masks is not None:
            include_masks -= exclude_masks

        if include_masks is not None:
            self.include_masks = set()
            for mask in include_masks:
                try:
                    self.include_masks.add(re.compile(mask))
                except Exception:
                    pass
            if len(self.include_masks) == 0:
                self.include_masks = None
        else:
            self.include_masks = None

        if exclude_masks is not None:
            self.exclude_masks = set()
            for mask in exclude_masks:
                try:
                    self.exclude_masks.add(re.compile(mask))
                except Exception:
                    pass
            if len(self.exclude_masks) == 0:
                self.exclude_masks = None
        else:
            self.exclude_masks = None

        self.search_type = search_type
        self.hash_method = hash_method
        self.depth = depth
        self.min_file_size = min_file_size
        self.blocksize = blocksize
        self.include_directories = include_directories
        self.exclude_directories = exclude_directories
        self.files_to_scan = set()
        self.duplicates = defaultdict(set)
        self.__thread_pool = QThreadPool()
        self.__mutex = QMutex()

    def find(self) -> defaultdict[Set]:
        for dir in self.include_directories:
            self.__scan_directory(dir, self.depth)
        self.__find_duplicates()
        return self.duplicates

    def __find_duplicates(self) -> None:
        if len(self.files_to_scan) < 2:
            return
        for filepath_1 in self.files_to_scan:
            for filepath_2 in self.files_to_scan:
                if filepath_1 == filepath_2:
                    continue
                worker = Worker(self.__check_for_duplicates, filepath_1, filepath_2)
                self.__thread_pool.start(worker)
        self.__thread_pool.waitForDone()

    def __check_for_duplicates(self, f1: os.path, f2: os.path, *args, **kwargs) -> None:
        if self.search_type == SearchTypes.BY_NAME:
            if os.path.basename(f1) == os.path.basename(f2):
                self.__add_to_duplicates(f1, f2)

        elif self.search_type == SearchTypes.BY_HASH:
            h1 = HashedFile(f1, self.hash_method, self.blocksize)
            h2 = HashedFile(f2, self.hash_method, self.blocksize)
            if h1 == h2:
                self.__add_to_duplicates(f1, f2)

    def __add_to_duplicates(self, f1: os.path, f2: os.path) -> None:
        f1 = os.path.abspath(f1)
        f2 = os.path.abspath(f2)
        if self.__already_in_duplicates(f1) and self.__already_in_duplicates(f2):
            return
        locker = QMutexLocker(self.__mutex)
        if f2 in self.duplicates:
            self.duplicates[f2].add(f1)
            return
        for key, value in self.duplicates.items():
            if f1 in value:
                self.duplicates[key].add(f2)
                return
            elif f2 in value:
                self.duplicates[key].add(f1)
                return
        self.duplicates[f1].add(f2)

    def __add_file(self, path: os.path, *args, **kwargs) -> None:
        def path_in_masks(p, masks):
            return any(bool(regex.match(os.path.basename(p))) for regex in masks)

        def can_add_file(path: os.path) -> bool:
            if self.min_file_size > 0 and os.stat(path).st_size < self.min_file_size:
                return False
            if self.include_masks is None and self.exclude_masks is None:
                return True
            if self.include_masks is not None and self.include_masks and self.exclude_masks is None:
                return path_in_masks(path, self.include_masks)
            if self.include_masks is None and self.exclude_masks and self.exclude_masks is not None:
                return not path_in_masks(path, self.exclude_masks)
            return path_in_masks(path, self.include_masks) and not path_in_masks(path, self.exclude_masks)

        if can_add_file(path):
            locker = QMutexLocker(self.__mutex)
            self.files_to_scan.add(path)

    def __scan_directory(self, path: os.path, depth: int, *args, **kwargs) -> None:
        if depth < 0:
            return
        if (self.exclude_directories is None) or (path not in self.exclude_directories):
            for p in os.scandir(path):
                if os.path.exists(p):
                    if os.path.isfile(p):
                        worker = Worker(self.__add_file, path=p)
                    else:
                        worker = Worker(self.__scan_directory, path=p, depth=depth - 1)
                    self.__thread_pool.start(worker)
            self.__thread_pool.waitForDone()

    def __already_in_duplicates(self, path: os.path) -> bool:
        if not self.duplicates:
            return False
        for key, value in self.duplicates.items():
            if path == key or path in value:
                return True
        return False
