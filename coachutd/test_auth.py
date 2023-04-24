from coachutd.models import User
from .test import get_test_client
from . import db

def test_login_incorrect():
    client = get_test_client()
    response = client.post( '/login', data=dict(username="test",
                                                password="test"))
    assert response.status_code == 403

def test_login_correct():
    client = get_test_client()

    with client.application.app_context():
        # create a user
        db.session.add(User(username="test", password="test"))

        response = client.post( '/login', data=dict(username="test",
                                                    password="test"))
        assert response.status_code == 200

def test_login_valid_valid():
    client = get_test_client()

    with client.application.app_context():
        # create a user
        db.session.add(User(username="Jonathan", password="Hello123"))

        response = client.post( '/login', data=dict(username="Jonathan",
                                                    password="Hello123"))
        assert response.status_code == 200


def test_login_valid_invalid():
    client = get_test_client()

    with client.application.app_context():
        # create a user
        db.session.add(User(username="Jonathan", password="Hello123"))

        response = client.post( '/login', data=dict(username="Jonathan",
                                                    password="Hell123"))
        assert response.status_code == 403

def test_login_invalid_valid():
    client = get_test_client()

    with client.application.app_context():
        # create a user
        db.session.add(User(username="Jonatan", password="Hello123"))

        response = client.post( '/login', data=dict(username="Jonathan",
                                                    password="Hell123"))
        assert response.status_code == 403

