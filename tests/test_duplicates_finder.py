from duplicates_finder import DuplicatesFinder
from search_types import SearchTypes
from thread_safe_dict import ThreadSafeDict


def compare_random_dicts(result, expected):
    for key in result:
        assert key in expected
    for key in expected:
        assert key in result
    for key, value in expected.items():
        assert set(value) == set(result[key])


def test_find_by_hash(temp_duplicates):
    _, files = temp_duplicates
    f1, f2, f3, f4, f5, f6, f7, f8, f9 = files
    expected = ThreadSafeDict({
        str(f1): [str(f4), str(f8)],
        str(f2): [str(f3), str(f7)],
        str(f9): [str(f5), str(f6)],
    })
    finder = DuplicatesFinder()
    finder.find_duplicates(files, SearchTypes.BY_HASH)
    result = finder._DuplicatesFinder__duplicates
    compare_random_dicts(result, expected)


def test_find_by_name(temp_duplicates):
    _, files = temp_duplicates
    f1, f2, f3, f4, f5, f6, f7, f8, f9 = files
    expected = ThreadSafeDict({
        str(f1): [str(f3)],
        str(f4): [str(f5)],
    })
    finder = DuplicatesFinder()
    finder.find_duplicates(files, SearchTypes.BY_NAME)
    result = finder._DuplicatesFinder__duplicates
    compare_random_dicts(result, expected)
