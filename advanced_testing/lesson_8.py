import os
from unittest.mock import Mock
from functions import get_function

get_files_count = get_function()


def get_fixture_path(name):
    return os.path.join('fixtures', name)


# BEGIN (write your solution here)
def test_get_files_count():
    flat_structure = get_fixture_path('flat')

    mock = Mock()
    get_files_count(flat_structure, mock)
    assert mock.call_count == 1
    args_list = [value for key, value in mock.call_args_list]
    assert args_list == [('Go!',)]
# END
