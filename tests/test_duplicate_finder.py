import os
from pprint import pprint

import pytest
from PySide6.QtCore import QCryptographicHash

from duplicate_finder import DuplicateFinder, SearchTypes


def list_of_sets_are_equal(l1, l2):
    if len(l1) != len(l2):
        return False
    for v1 in l1:
        if v1 not in l2:
            return False
    for v2 in l2:
        if v2 not in l1:
            return False
    return True


@pytest.mark.parametrize("hash_method", [
    QCryptographicHash.Algorithm.Md5,
    QCryptographicHash.Algorithm.Sha1,
    QCryptographicHash.Algorithm.Sha512
])
@pytest.mark.parametrize("blocksize", [
    1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1000, 1024
])
@pytest.mark.parametrize(
    "search_type, expected_files, exclude_directories, include_masks, exclude_masks, min_file_size, depth", [
        (SearchTypes.BY_HASH, [{0, 3, 7}, {1, 2, 6}, {4, 5, 8}], None, None, None, 0, 0),
        (SearchTypes.BY_HASH, [], {0, 1, 2, 3, 4}, None, None, 0, 0),
        (SearchTypes.BY_HASH, [{0, 3}, {1, 2}, {4, 5}], {4}, {"[123]", "4"}, {"[123"}, 0, 0),
        (SearchTypes.BY_HASH, [{0, 3, 7}, {1, 2, 6}, {4, 5, 8}], None, {"[123"}, None, 0, 0),
        (SearchTypes.BY_HASH, [{0, 3}, {1, 2}, {4, 5}], None, {"[123]", "4"}, None, 0, 0),
        (SearchTypes.BY_HASH, [{3, 7}, {2, 6}], {0, 2}, None, None, 0, 0),
        (SearchTypes.BY_HASH, [{3, 7}], {0, 2}, None, {"[12]", "4"}, 0, 0),
        (SearchTypes.BY_HASH, [{3, 7}], {0, 2}, {"[123456]"}, {"[12]", "4"}, 0, 0),
        (SearchTypes.BY_HASH, [], {0, 2}, {"[123456]"}, {"[12]", "4"}, 2 ** 32, 0),
        (SearchTypes.BY_HASH, [{3, 7}, {2, 6}, {4, 5, 8}], {0}, None, None, 0, 0),
        (SearchTypes.BY_NAME, [{0, 2}, {3, 4}], None, None, None, 0, 0),
        (SearchTypes.BY_NAME, [], {0, 2}, None, None, 0, 0)
    ])
def test_find(search_type,
              expected_files,
              exclude_directories,
              temp_duplicates,
              include_masks,
              exclude_masks,
              min_file_size,
              depth,
              blocksize,
              hash_method):
    dirs, files = temp_duplicates
    expected_files = sorted([{os.path.abspath(files[i]) for i in s} for s in expected_files])
    if exclude_directories is not None:
        exclude_directories = {dirs[i] for i in exclude_directories}

    finder = DuplicateFinder(search_type,
                             include_directories=set(dirs),
                             exclude_directories=exclude_directories,
                             include_masks=include_masks,
                             exclude_masks=exclude_masks,
                             min_file_size=min_file_size,
                             depth=depth,
                             blocksize=blocksize,
                             hash_method=hash_method)
    result = sorted([set(value).union({key}) for key, value in finder.find().items()])
    try:
        assert list_of_sets_are_equal(result, expected_files)
    except AssertionError:
        pprint("")
        pprint("Assertion error. Data Mismatch:")
        pprint("Result:")
        pprint(result)
        pprint("Expected:")
        pprint(expected_files)
        raise


@pytest.mark.raises
def test_raise_on_empty_include_dirs():
    with pytest.raises(ValueError):
        DuplicateFinder(include_directories=None)
