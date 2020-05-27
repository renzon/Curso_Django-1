import django.test


def test_status_code(client: django.test.Client):
    resp = client.get('/')
    assert resp.status_code == 200
