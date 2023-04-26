from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True)
    username = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    about = db.Column(db.Text)
    age = db.Column(db.Integer)
    sex = db.Column(db.Text)
    availability = db.Column(db.Text)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.ForeignKey("user.id"))
    body = db.Column(db.Text)
    # comma separated list of days represented by first two letters of day (like "Mo,Th")
    availability = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())


class Like(db.Model):
    user = db.Column(db.ForeignKey("user.id"), primary_key=True)
    post = db.Column(db.ForeignKey("post.id"), primary_key=True)
