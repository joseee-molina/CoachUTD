from flask import session
from flask_login import login_user
from sqlalchemy import insert, select
from werkzeug.security import generate_password_hash
from coachutd.models import User
from .test import *
from . import db


def test_update_bio(client):
    with client.application.app_context(), client.application.test_request_context():
        # add the user
        db.session.add(
            User(
                username="test",
                password=generate_password_hash("test"),
                bio="old value",
            )
        )
        # fetch the user
        user = db.session.get(User, 1)
        assert user is not None
        assert user.bio == "old value"
        # log the user in
        assert login_user(user)

        # try to update the user profile
        response = client.post("/profile/", data={"bio": "new value"})

        print(response.data)
        # expect updated user
        assert response.request.path == "/profile/"
        assert response.status_code == 302
        # assert "new value" in response.data
        # # FIXME: uncomment when profile data is loaded into page


def test_change_sports_preferences_changed(client):
    with client.application.app_context(), client.application.test_request_context():
        # add the user
        db.session.add(
            User(
                username="Jonathan",
                password=generate_password_hash("Hello123"),
            )
        )
        user = db.session.get(User, 1)
        assert user is not None
        assert user.tennis == False
        assert login_user(user)
        response = client.post("/profile/", data=dict(tennis=True))

        assert user.tennis == True
        print(response.data)
        assert response.request.path == "/profile/"
        assert response.status_code == 302

        # # FIXME: uncomment when profile data is loaded into page


def test_change_sports_preferences_unchanged(client):
    with client.application.app_context(), client.application.test_request_context():
        # add the user
        db.session.add(
            User(
                username="Jonathan",
                password=generate_password_hash("Hello123"),
            )
        )
        user = db.session.get(User, 1)
        assert user is not None
        assert user.tennis == False
        assert login_user(user)
        response = client.post("/profile/", data=dict(tennis=False))

        assert user.tennis == True
        print(response.data)
        assert response.request.path == "/profile/"
        assert response.status_code == 302

        # # FIXME: uncomment when profile data is loaded into page
