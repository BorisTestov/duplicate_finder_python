from __future__ import annotations

import os
from collections import deque
from math import ceil

from PySide6.QtCore import QIODevice, QObject, QByteArray, QCryptographicHash, QFile


class HashedFile(QObject):
    __slots__ = ('__blocksize', '__filepath',
                 '__hash_method', '__hash_data',
                 '__filesize', '__max_blocks_amount')

    def __init__(self, path: os.path,
                 hash_method: QCryptographicHash.Algorithm = QCryptographicHash.Algorithm.Md5,
                 blocksize: int = 512):
        super().__init__()
        if blocksize < 1:
            raise ValueError("Size of block must be positive")
        if not os.path.exists(path):
            raise FileNotFoundError(f"Path {path} doesn't exist")
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Path {path} is a directory")
        self.__blocksize = blocksize
        self.__filepath = path
        self.__hash_method = hash_method
        self.__hash_data = deque()
        self.__filesize = os.stat(self.__filepath).st_size
        self.__max_blocks_amount = ceil(self.__filesize / self.__blocksize)

    def __eq__(self, other: HashedFile) -> bool:
        if self.get_file_size() != other.get_file_size():
            return False
        for i in range(self.__max_blocks_amount):
            if self.get_hash_node(i) != other.get_hash_node(i):
                return False
        return True

    def get_file_path(self) -> os.path:
        return self.__filepath

    def get_file_size(self) -> int:
        return self.__filesize

    def get_hash_node(self, block_index: int) -> QByteArray:
        if block_index >= self.__max_blocks_amount or block_index < 0:
            raise ValueError("Invalid block index value")
        if block_index >= len(self.__hash_data):
            self.__calculate_hash_until(block_index)
        return self.__hash_data[block_index]

    def __calculate_hash_until(self, block_index: int) -> None:
        file = QFile(self.get_file_path())
        file.open(QIODevice.OpenModeFlag.ReadOnly)
        while len(self.__hash_data) <= block_index:
            file.seek(self.__blocksize * len(self.__hash_data))
            data = file.read(self.__blocksize)
            self.__hash_data.append(QCryptographicHash.hash(data, self.__hash_method))
        file.close()
