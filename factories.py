import os

from hashed_file import HashedFile
from search_types import SearchTypes


class TrieSplitMethodFactory:
    def __init__(self):
        self.__mapping = {
            SearchTypes.BY_HASH: self.__split_by_hash,
            SearchTypes.BY_NAME: self.__split_by_name
        }

    def __getitem__(self, item):
        return self.__mapping.get(item, None)

    def __split_by_hash(self, hfile: HashedFile):
        while not hfile.end_of_file():
            yield hfile.get_chunk_hash()

    def __split_by_name(self, hfile: HashedFile):
        yield hfile.get_base_name()


class FileGrouperFactory:
    __mapping = {
        SearchTypes.BY_HASH: lambda path: os.stat(path).st_size,
        SearchTypes.BY_NAME: lambda path: os.path.splitext(path)[-1]
    }

    @classmethod
    def __class_getitem__(cls, item):
        return cls.__mapping.get(item, None)
