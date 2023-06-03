import os
from string import ascii_uppercase

import pytest

from hashed_file import HashedFile


def test_file_size(temp_file):
    for i in range(len(ascii_uppercase)):
        content = ascii_uppercase[:i + 1]
        with open(temp_file, "w") as f:
            print(content, file=f)
        hashed_file = HashedFile(temp_file)
        assert hashed_file.get_file_size() == len(content) + 2


def test_file_path(temp_file):
    for i in range(len(ascii_uppercase)):
        content = ascii_uppercase[:i + 1]
        with open(temp_file, "w") as f:
            print(content, file=f)
        hashed_file = HashedFile(temp_file)
        assert hashed_file.get_file_path() == temp_file


def test_on_empty_files(paired_temp_file):
    f1, f2 = paired_temp_file
    with open(f1, "w"):
        pass
    with open(f2, "w"):
        pass
    hashed_file_1 = HashedFile(f1)
    hashed_file_2 = HashedFile(f2)
    assert hashed_file_1 == hashed_file_2


def test_unequality_on_different_size(paired_temp_file):
    f1, f2 = paired_temp_file
    with open(f1, "w") as f:
        print("A", file=f)
    with open(f2, "w") as f:
        print("AB", file=f)
    assert HashedFile(f1) != HashedFile(f2)


def test_unequality_on_different_content(paired_temp_file):
    f1, f2 = paired_temp_file
    with open(f1, "w") as f:
        print("A", file=f)
    with open(f2, "w") as f:
        print("B", file=f)
    assert HashedFile(f1) != HashedFile(f2)


@pytest.mark.parametrize("blocksize", [1, 10, 100, 512, 1024])
def test_hash(paired_temp_file, blocksize):
    f1, f2 = paired_temp_file
    for i in range(len(ascii_uppercase)):
        content = ascii_uppercase[:i + 1]
        with open(f1, "w") as f:
            print(content, file=f)
        with open(f2, "w") as f:
            print(content, file=f)
        hashed_file_1 = HashedFile(f1, blocksize=blocksize)
        hashed_file_2 = HashedFile(f2, blocksize=blocksize)
        assert hashed_file_1 == hashed_file_2


@pytest.mark.raises
def test_raise_on_incorrect_file():
    with pytest.raises(FileNotFoundError):
        HashedFile("INCORRECT_FILE_NAME")


@pytest.mark.raises
@pytest.mark.parametrize("blocksize", [0, -1, -5, -100])
def test_raise_on_incorrect_blocksize(temp_file, blocksize):
    with open(temp_file, "w"):
        pass
    with pytest.raises(ValueError):
        HashedFile(temp_file, blocksize=blocksize)


@pytest.mark.raises
def test_raise_on_directory(temp_file):
    filepath = os.path.dirname(temp_file)
    with pytest.raises(FileNotFoundError):
        HashedFile(filepath)


@pytest.mark.raises
@pytest.mark.parametrize("blockindex", [-1, -5, 2 ** 32])
def test_raise_on_invalid_block_index(temp_file, blockindex):
    with open(temp_file, "w") as f:
        print("TEST", file=f)
    hashed_file = HashedFile(temp_file)
    with pytest.raises(ValueError):
        hashed_file.get_hash_node(blockindex)
