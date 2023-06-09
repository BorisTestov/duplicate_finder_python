import logging
import os
import re
from collections import deque
from typing import Set, Union

from PySide6.QtCore import Signal

from interruptible_class import InterruptibleClass
from thread_safe_set import ThreadSafeSet


class DirectoryScanner(InterruptibleClass):
    all_files_added = Signal(deque)

    def __init__(self):
        # QObject.__init__(self)
        InterruptibleClass.__init__(self, parent=self)
        self._depth = 0
        self._min_file_size = 0
        self._include_directories = None
        self._exclude_directories = None
        self._include_masks = None
        self._exclude_masks = None
        self._files_to_scan = ThreadSafeSet()

    def scan(self):
        logging.info("Directory scanner started")
        self._files_to_scan.clear()
        for dir in self._include_directories:
            self._add_task(self.__scan_directory, dir, self._depth)
        self._wait_for_tasks_completion()
        logging.info("All directories scanned")
        self.all_files_added.emit(self._files_to_scan)

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, value):
        self._depth = value

    @property
    def min_file_size(self):
        return self._min_file_size

    @min_file_size.setter
    def min_file_size(self, value):
        self._min_file_size = value

    @property
    def include_directories(self):
        return self._include_directories

    @include_directories.setter
    def include_directories(self, directories):
        self._include_directories = self.__process_directories(directories)

    @property
    def exclude_directories(self):
        return self._exclude_directories

    @exclude_directories.setter
    def exclude_directories(self, directories):
        self._exclude_directories = self.__process_directories(directories)

    @property
    def include_masks(self):
        return self._include_masks

    @include_masks.setter
    def include_masks(self, masks):
        self._include_masks = self.__process_masks(masks)

    @property
    def exclude_masks(self):
        return self._exclude_masks

    @exclude_masks.setter
    def exclude_masks(self, masks):
        self._exclude_masks = self.__process_masks(masks)

    def __process_directories(self, directories: Union[Set, None]) -> Union[Set, None]:
        if directories is not None:
            return set(dir for dir in directories if os.path.exists(dir) and os.path.isdir(dir))
        else:
            return None

    def __process_masks(self, masks: Union[Set, None]) -> Union[Set, None]:
        if masks is not None:
            compiled_masks = set()
            for mask in masks:
                try:
                    compiled_masks.add(re.compile(mask))
                except re.error:
                    pass
            return compiled_masks if compiled_masks else None
        else:
            return None

    def __can_add_file(self, path: os.path) -> bool:
        def path_in_masks(p, masks):
            return any(regex.match(os.path.basename(p)) for regex in masks)

        if self.min_file_size > 0 and os.stat(path).st_size < self.min_file_size:
            return False
        include_condition = self.include_masks is None or path_in_masks(path, self.include_masks)
        exclude_condition = self.exclude_masks is None or not path_in_masks(path, self.exclude_masks)
        return include_condition and exclude_condition

    def __can_read(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return True
        except IOError:
            return False

    def __scan_directory(self, path: os.path, depth: int) -> None:
        queue = deque([(path, depth)])
        while queue:
            if self.need_to_interrupt():
                return
            path, current_depth = queue.popleft()
            if current_depth < 0:
                continue
            if self.exclude_directories is not None and path in self.exclude_directories:
                continue
            try:
                subdirs = self.__handle_directory(path)
                queue.extend((subdir, current_depth - 1) for subdir in subdirs)
            except PermissionError as e:
                logging.error(f"Permission denied: {path}, Error: {e}")
            except Exception as e:
                logging.error(f"An error occurred during scanning: {str(e)}")

    def __handle_directory(self, path):
        if not os.access(path, os.R_OK):
            raise PermissionError(f"Cannot read directory: {path}")
        subdirs = []
        for p in os.scandir(path):
            if not os.path.exists(p.path):
                continue
            if os.path.isfile(p.path):
                self.__handle_file(p.path)
            else:
                subdirs.append(p.path)
        return subdirs

    def __handle_file(self, path):
        if not self.__can_add_file(path):
            return
        if not self.__can_read(path):
            logging.error(f"Can't read file {path}. Check permissions.")
            return
        self._files_to_scan.add(path)
