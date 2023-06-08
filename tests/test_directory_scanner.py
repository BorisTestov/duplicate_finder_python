from directory_scanner import DirectoryScanner
from thread_safe_set import ThreadSafeSet


def test_directory_scanner(temp_duplicates):
    directories, files = temp_duplicates
    scanner = DirectoryScanner()
    scanner.include_directories = directories
    scanner.scan()
    result = scanner._files_to_scan
    expected = ThreadSafeSet([str(x) for x in files])
    assert result == expected
