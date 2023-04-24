from flask import Blueprint, request
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

    user = User.query.filter_by(username=username).one()
    user.age = age
    user.sex = sex
    user.availability = availability




    return "Success", 200
