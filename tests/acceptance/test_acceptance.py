import pytest
import requests

base_url = 'http://localhost:5000'


@pytest.fixture
def user():
    return {
        'name': 'John',
        'login': 'john@lennon.com',
        'password': 'yoko123'
    }


def test_create_collection(user):
    response = requests.post(base_url + '/users', data=user)
    assert response.status_code == 201
    json = response.json()
    assert 'id' in json
    assert json['login'] == user['login']
    assert json['name'] == user['name']
    assert json['password'] == user['password']


def test_get_collection(user):
    test_create_collection(user)
    response = requests.get(base_url + '/users')
    assert response.status_code == 200
    json = response.json()
    assert isinstance(json, list)
    assert len(json) > 0
