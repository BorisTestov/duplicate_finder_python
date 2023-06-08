from __future__ import annotations

import os
from collections import deque
from math import ceil

import xxhash
from PySide6.QtCore import QByteArray
from PySide6.QtCore import QObject, QFile, QIODevice


class HashedFile(QObject):
    __slots__ = ('__blocksize', '__filepath', '__file_handle', '__hash_method',
                 '__hash_data', '__filesize', '__max_blocks_amount')

    def __init__(self, path: os.path):
        super(HashedFile, self).__init__()
        self.__blocksize = 512
        self.__filepath = path
        self.__hasher = xxhash.xxh64()
        self.__hash_data = deque()
        self.__filesize = os.stat(self.__filepath).st_size
        self.__max_blocks_amount = ceil(self.__filesize / self.__blocksize)

    def __enter__(self):
        try:
            self.__file_handle = QFile(self.get_file_path())
            self.__file_handle.open(QIODevice.ReadOnly)
        except Exception as e:
            print(e)
            raise
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__file_handle:
            self.__file_handle.close()

    def __eq__(self, other: HashedFile) -> bool:
        if self.get_file_size() != other.get_file_size():
            return False
        for i in range(self.__max_blocks_amount):
            if self.get_hash_node(i) != other.get_hash_node(i):
                return False
        return True

    def __hash__(self):
        return hash(self.get_file_path())

    def get_file_path(self) -> os.path:
        return os.path.abspath(self.__filepath)

    def get_file_size(self) -> int:
        return self.__filesize

    def get_hash_node(self, block_index: int) -> QByteArray:
        if block_index >= self.__max_blocks_amount or block_index < 0:
            raise ValueError("Invalid block index value")
        if block_index >= len(self.__hash_data):
            self.get_chunk_hash()
        return self.__hash_data[block_index]

    def get_chunk_hash(self):
        self.__file_handle.seek(self.__blocksize * len(self.__hash_data))
        data = self.__file_handle.read(self.__blocksize)
        self.__hasher.update(data.data())
        hash = self.__hasher.hexdigest()
        self.__hash_data.append(hash)
        return hash

    def get_base_name(self):
        return os.path.basename(self.get_file_path())

    def reset(self):
        self.__file_handle.seek(0)
        self.__hash_data.clear()

    def end_of_file(self) -> bool:
        return self.__file_handle.atEnd()
