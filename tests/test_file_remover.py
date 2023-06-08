import os

from file_remover import FileRemover


def test_file_remover(temp_duplicates):
    files, _ = temp_duplicates
    file_remover = FileRemover()
    file_remover.remove_files(files)
    for file in files:
        assert not os.path.exists(file)
