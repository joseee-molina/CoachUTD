from flask import session
from flask_login import login_user
from sqlalchemy import insert, select
from werkzeug.security import generate_password_hash
from coachutd.models import User
from .test import *
from . import db


def test_create_post_valid(client):
    with client.application.app_context(), client.application.test_request_context():
        # add the user
        db.session.add(
            User(
                username="test2",
                password=generate_password_hash("Hello123"),
                
            )
        )
        user = db.session.get(User, 1)
        assert user is not None
        assert login_user(user)
        
        # try to create post
        response = client.post("/explore/create/", data={"body": "hello this is a new post", "mon" : True ,"tue" : True ,"wed": True})
        print(response.data)
        # creeated post asserts
        assert response.request.path == "/explore/create/"
        assert response.status_code == 303
        # assert "new value" in response.data 
        # # FIXME: uncomment when profile data is loaded into page

def test_create_post_invalid_1(client):
    with client.application.app_context(), client.application.test_request_context():
        # add the user
        db.session.add(
            User(
                username="test3",
                password=generate_password_hash("Hello123"),
                bio="old value",
            )
        )
        user = db.session.get(User, 1)
        assert user is not None
        assert login_user(user)
        
        # try to create post
        response = client.post("/explore/create/", data={"body": "", "availability": ["mon","tue","wed"]})
        print(response.data)
        # creeated post asserts
        assert response.request.path == "/explore/create/"
        assert response.status_code == 400
        # assert "new value" in response.data 
        # # FIXME: uncomment when profile data is loaded into page

def test_create_post_invalid_2(client):
    with client.application.app_context(), client.application.test_request_context():
        # add the user
        db.session.add(
            User(
                username="test4",
                password=generate_password_hash("Hello123"),
                bio="old value",
            )
        )
        user = db.session.get(User, 1)
        assert user is not None
        assert login_user(user)
        
        # try to create post
        response = client.post("/explore/create/", data={"body": "   ", "availability": ["mon","tue","wed"]})
        print(response.data)
        # creeated post asserts
        assert response.request.path == "/explore/create/"
        assert response.status_code == 400
        # assert "new value" in response.data 
        # # FIXME: uncomment when profile data is loaded into page
