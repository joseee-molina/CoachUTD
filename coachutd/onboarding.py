from flask import Blueprint, request
from . import db
from .models import User

onboarding = Blueprint('onboarding', __name__)

@onboarding.route('/onboarding', methods=['POST'])
def set_personal_information():
    # change about field of user
    username = request.form.get('username')
    password = request.form.get('password')
    age = request.form.get('age')
    sex = request.form.get('sex')
    availability = request.form.get('availability')

    User.query.filter_by(username=username).first().age = age
    User.query.filter_by(username=username).first().sex = sex
    User.query.filter_by(username=username).first().availability = availability



    return "Success", 200
