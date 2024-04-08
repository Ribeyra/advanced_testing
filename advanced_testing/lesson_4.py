import os
from functions import get_function

prettify_html_file = get_function()


# BEGIN (write your solution here)
raw = 'before.html'

prepared = 'after.html'


def read_file(path):
    with open(path) as file:
        return file.read()


def collect_path(name, directory='fixtures'):
    return os.path.join(directory, name)


def test_formater(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / raw
    p.write_text(read_file(collect_path(raw)))
    prettify_html_file(p)
    assert p.read_text() == read_file(collect_path(prepared))
# END
