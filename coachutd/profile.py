from flask import Blueprint, request
from . import db
from .models import User

profile = Blueprint('profile', __name__)

@profile.route('/about', methods=['POST'])
def change_description():
    # change about field of user
    about = request.form.get('about')
    username = request.form.get('username')
    password = request.form.get('password')

    User.query.filter_by(username=username).first().about = about

    return "Success", 200
