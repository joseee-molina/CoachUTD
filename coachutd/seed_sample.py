from werkzeug.security import generate_password_hash
from coachutd.models import User, Post, Like


def seed(session):
    users = [
        User(
            id=1,
            username="test",
            password=generate_password_hash("test"),
            about="test user",
            age=20,
            sex="M",
            availability="Mo,We,Fr",
            coach=True,
            trainee=True,
        ),
        User(
            id=2,
            username="test2",
            password=generate_password_hash("test2"),
            about="test user 2",
            age=20,
            sex="F",
            availability="Tu,Th,Sa",
            coach=True,
            trainee=False,
        ),
        User(
            id=3,
            username="test3",
            password=generate_password_hash("test3"),
            about="test user 3",
            age=20,
            availability="Mo,We,Fr",
            coach=False,
            trainee=True,
        ),
    ]

    posts = [
        Post(
            id=1,
            author=1,
            body="test post",
            availability="Mo,We,Fr",
        ),
        Post(
            id=2,
            author=2,
            body="test post 2",
            availability="Tu,Th,Sa",
        ),
        Post(
            id=3,
            author=3,
            body="test post 3",
            availability="Mo,We,Fr",
        ),
    ]

    likes = [
        Like(
            user=1,
            post=2,
        ),
        Like(
            user=2,
            post=1,
        ),
        Like(
            user=3,
            post=1,
        ),
    ]

    with session.begin():
        session.add_all(users)
        session.add_all(posts)
        session.add_all(likes)
