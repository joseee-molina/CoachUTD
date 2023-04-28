from collections import namedtuple
from sqlalchemy.ext.hybrid import hybrid_property
from flask_login import UserMixin
from . import db

Availability = namedtuple(
    "Availability", ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
)


def bits_to_availability(bits):
    availability = [bool((bits >> i) & 1) for i in range(0, 7)]
    return Availability(*availability)


def availability_to_bits(availability):
    bits = [int(availability[i]) << i for i in range(0, 7)]
    return sum(bits)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    coach = db.Column(db.Boolean, default=False)
    trainee = db.Column(db.Boolean, default=False)
    bio = db.Column(db.Text)
    age = db.Column(db.Integer)
    sex = db.Column(db.Text)
    _availability = db.Column("availability", db.SmallInteger)
    """Represented as bitfield of width 7, mapped to a named tuple"""

    @hybrid_property
    def availability(self):
        return bits_to_availability(self._availability)

    @availability.inplace.setter
    def _availability_setter(self, availability):
        self._availability = availability_to_bits(availability)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.ForeignKey("user.id"))
    body = db.Column(db.Text)
    _availability = db.Column("availability", db.SmallInteger)
    """Represented as bitfield of width 7, mapped to a named tuple"""

    @hybrid_property
    def availability(self):
        return bits_to_availability(self._availability)

    @availability.inplace.setter
    def _availability_setter(self, availability):
        self._availability = availability_to_bits(availability)

    created_at = db.Column(db.DateTime, server_default=db.func.now())


class Like(db.Model):
    user = db.Column(db.ForeignKey("user.id"), primary_key=True)
    post = db.Column(db.ForeignKey("post.id"), primary_key=True)
