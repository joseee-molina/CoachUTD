from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    coach = db.Column(db.Boolean, default=False)
    trainee = db.Column(db.Boolean, default=False)
    bio = db.Column(db.Text)
    # availability
    mon = db.Column(db.Boolean, default=False)
    tue = db.Column(db.Boolean, default=False)
    wed = db.Column(db.Boolean, default=False)
    thu = db.Column(db.Boolean, default=False)
    fri = db.Column(db.Boolean, default=False)
    sat = db.Column(db.Boolean, default=False)
    sun = db.Column(db.Boolean, default=False)
    # sports
    tennis = db.Column(db.Boolean, default=False)
    soccer = db.Column(db.Boolean, default=False)
    basketball = db.Column(db.Boolean, default=False)
    baseball = db.Column(db.Boolean, default=False)
    other_sport = db.Column(db.Text)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.ForeignKey("user.id"))
    body = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    # availability
    mon = db.Column(db.Boolean, default=False)
    tue = db.Column(db.Boolean, default=False)
    wed = db.Column(db.Boolean, default=False)
    thu = db.Column(db.Boolean, default=False)
    fri = db.Column(db.Boolean, default=False)
    sat = db.Column(db.Boolean, default=False)
    sun = db.Column(db.Boolean, default=False)


class Sport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.ForeignKey("user.id"))
    tennis = db.Column(db.Boolean, default=False)
    soccer = db.Column(db.Boolean, default=False)
    basketball = db.Column(db.Boolean, default=False)
    baseball = db.Column(db.Boolean, default=False)
    other_sport = db.Column(db.Text)


class Like(db.Model):
    user = db.Column(db.ForeignKey("user.id"), primary_key=True)
    post = db.Column(db.ForeignKey("post.id"), primary_key=True)
