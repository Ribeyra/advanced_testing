""" with open('fixtures/result.html') as file:
    result = file.read()


def test_yaml_to_html():
    with open('fixtures/list.yaml') as file:
        yaml = file.read()

    assert f"{to_html_list('fixtures/list.yaml')}\n" == result


def test_json_to_html():
    with open('fixtures/list.json') as file:
        json = file.read()

    assert f"{to_html_list('fixtures/list.json')}\n" == result


def test_csv_to_html():
    with open('fixtures/list.csv') as file:
        csv = file.read()

    assert f"{to_html_list('fixtures/list.csv')}\n" == result """
import os


def to_html_list(path):
    pass


def get_path(name):
    return os.path.join('fixtures', name)


with open('fixtures/result.html') as file:
    result = file.read().strip()


def test_yaml_to_html():
    path = get_path('list.yaml')
    assert to_html_list(path) == result


def test_json_to_html():
    path = get_path('list.json')
    assert to_html_list(path) == result


def test_csv_to_html():
    path = get_path('list.csv')
    assert to_html_list(path) == result
