from werkzeug.security import generate_password_hash
from coachutd.models import User
from .test import *
from . import db


def test_login_incorrect(client):
    with client.application.app_context():
        response = client.post("/login/", data=dict(username="Jonathan", password="Hello123"))
        assert response.status_code == 403



def test_login_correct(client):
    with client.application.app_context():
        # create a user
        db.session.add(User(username="test", password=generate_password_hash("test")))

        response = client.post("/login/", data=dict(username="test", password="test"))
        assert response.status_code == 302


def test_login_valid_valid(client):
    with client.application.app_context():
        # create a user
        db.session.add(
            User(username="Jonathan", password=generate_password_hash("Hello123"))
        )

        response = client.post(
            "/login/", data=dict(username="Jonathan", password="Hello123")
        )
        assert response.status_code == 302
        assert "explore" in response.location


def test_login_valid_invalid(client):
    with client.application.app_context():
        # create a user
        db.session.add(User(username="Jonathan", password="Hello123"))

        response = client.post(
            "/login/", data=dict(username="Jonathan", password="Hell123")
        )
        assert response.status_code == 403


def test_login_invalid_valid(client):
    with client.application.app_context():
        # create a user
        db.session.add(User(username="Jonatan", password="Hello123"))

        response = client.post(
            "/login/", data=dict(username="Jonathan", password="Hell123")
        )
        assert response.status_code == 403
