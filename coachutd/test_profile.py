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
        response = client.post("/profile", data={"bio": "new value"})

        # expect updated user
        assert response.status_code == 200
        assert response.request.path == "/profile"
        # assert b"new value" in response.data # FIXME: uncomment when profile data is loaded into page
