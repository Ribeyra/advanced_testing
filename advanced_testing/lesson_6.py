# BEGIN FakeClient
class FakeClient:
    def __init__(self, data):
        self.data = data

    def list_for_users(self, user_name):
        return self.data
# END


def get_user_main_language(user_name, client=default_client):   # noqa F821
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
def test_get_user_main_language():
    USER_NAME = 'some'
    data0 = []
    empty_client = FakeClient(data0)
    assert get_user_main_language(USER_NAME, empty_client) is None

    data1 = [{"language": "php"}, {"language": "js"}, {"language": "js"}]
    client = FakeClient(data1)
    assert get_user_main_language(USER_NAME, client) == 'js'
# END
