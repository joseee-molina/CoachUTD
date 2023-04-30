from werkzeug.security import generate_password_hash
from coachutd.models import User, Post, Like


def seed(session):
    users = [
        User(
            id=1,
            username="test",
            password=generate_password_hash("test"),
            bio="test user",
            coach=True,
            trainee=True,
            mon=True,
            tue=True,
            sat=True,
        ),
        User(
            id=2,
            username="test2",
            password=generate_password_hash("test2"),
            bio="test user 2",
            coach=True,
            trainee=False,
        ),
        User(
            id=3,
            username="test3",
            password=generate_password_hash("test3"),
            bio="test user 3",
            coach=False,
            trainee=True,
        ),
    ]

    posts = [
        Post(
            id=1,
            author=1,
            body="test post",
        ),
        Post(
            id=2,
            author=2,
            body="test post 2",
        ),
        Post(
            id=3,
            author=3,
            body="test post 3",
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
