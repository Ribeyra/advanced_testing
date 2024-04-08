import os
from functions import get_function  # noqa F401


def _right(filepath, log=default_logger):   # noqa F821
    log()
    files_count = sum(len(files) for _, _, files in os.walk(filepath))
    return files_count


get_files_count = _right


# BEGIN (write your solution here)
def fake_log():
    pass


def get_path(name, path='fixtures'):
    return os.path.join(path, name)


def test_get_files_count():
    flat_structure = get_path('flat')
    assert get_files_count(flat_structure, fake_log) == 2

    nested_structure = get_path('nested')
    assert get_files_count(nested_structure, fake_log) == 4
# END
