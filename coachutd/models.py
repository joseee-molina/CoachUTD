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
