import os
import random
import string

import pytest


@pytest.fixture
def temp_file(tmp_path_factory):
    filename = tmp_path_factory.mktemp("data-") / ".testfile"
    return filename


@pytest.fixture
def paired_temp_file(tmp_path_factory):
    filename = tmp_path_factory.mktemp("data-") / ".testfile"
    filename_pair = tmp_path_factory.mktemp("data-") / ".testfile_paired"
    return filename, filename_pair


@pytest.fixture
def temp_duplicates(tmp_path_factory):
    d1 = tmp_path_factory.mktemp("A")
    d2 = tmp_path_factory.mktemp("B")
    d3 = tmp_path_factory.mktemp("C")
    d4 = tmp_path_factory.mktemp("D")
    d5 = d1 / 'A'
    os.mkdir(d5)

    f1 = d1 / '1'
    f2 = d1 / '2'
    f3 = d2 / '1'
    f4 = d2 / '3'
    f5 = d3 / '3'
    f6 = d3 / '4'
    f7 = d4 / '5'
    f8 = d4 / '6'
    f9 = d5 / '7'

    """
    f1, f4, f8 - duplicates by hash (A/1, B/3, D/6)
    f2, f3, f7 - duplicates by hash (A/2, B/1, D/5) 
    f5, f6, f9 - duplicates by hash (C/3, C/4, A/A/7)
    f1, f3 - duplicates by name (A/1, B/1)
    f4, f5 - duplicates by name (B/3, C/3)
    """
    n = 2000
    data = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))
    for file in (f1, f4, f8):
        with open(file, 'w') as f:
            print(data, file=f)
    data = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))
    for file in (f2, f3, f7):
        with open(file, 'w') as f:
            print(data, file=f)
    data = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))
    for file in (f5, f6, f9):
        with open(file, 'w') as f:
            print(data, file=f)
    dirs = [d1, d2, d3, d4, d5]
    files = [f1, f2, f3, f4, f5, f6, f7, f8, f9]
    return dirs, files
