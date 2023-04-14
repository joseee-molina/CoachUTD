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

