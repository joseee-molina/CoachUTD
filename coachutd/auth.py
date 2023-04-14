from flask import Blueprint, request 
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    # login code goes here
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not password == user.password:
        return "Incorrect username or password", 403

    # if the above check passes, then we know the user has the right credentials
    return "Success", 200

