from faker import Faker
from schema import Schema
from re import match

faker = Faker()


def get_default_data():
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
    }


def build_user(data={}):
    default_data = get_default_data()
    return {**default_data, **data}


schema = Schema({
    'first_name': str,
    'last_name': str,
    'email': lambda x: match(r'^\S+@\S+\.\S+$', x)
})


def test_gen():
    assert schema.is_valid(build_user())


def test_random():
    assert build_user() != build_user()


def test_garant():
    value = {
        'first_name': 'John',
        'last_name': 'Cena',
        'email': 'john_c@example.org'
    }
    assert build_user(value) == value
