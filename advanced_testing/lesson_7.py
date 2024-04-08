class Client():
    def list_for_users(self, user_name):
        raise Exception("Can not send http request")


default_client = Client()


def get_user_main_language(user_name, client=default_client):
    data = client.list_for_users(user_name)
    if not data:
        return None

    languges = map(lambda repo: repo["language"], data)
    languages_count = {}
    for language in languges:
        if language not in languages_count:
            languages_count[language] = 1
        else:
            languages_count[language] += 1
    return max(languages_count, key=lambda k: languages_count[k])


# BEGIN (write your solution here)
def fake_method(data):
    def inner(self, user_name):
        return data
    return inner


def test_get_user_main_language():
    USER_NAME = 'some'
    data0 = []
    default_client.list_for_users = fake_method(data0)
    assert get_user_main_language(USER_NAME) is None

    data1 = [{"language": "php"}, {"language": "js"}, {"language": "js"}]
    default_client.list_for_users = fake_method(data1)
    assert get_user_main_language(USER_NAME) == 'js'
# END
