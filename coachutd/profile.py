from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from .models import User
from . import db

profile = Blueprint("profile", __name__)


@profile.route("/profile", methods=["GET", "POST"])
@login_required
def update():
    if request.method == "POST":
        # change about field of user
        about = request.values.get("about")
        age = request.values.get("age")
        sex = request.values.get("sex")

        user = User.query.get(current_user.id)
        if about is not None:
            user.about = about
        if age is not None:
            user.age = age
        if sex is not None:
            user.sex = sex

        user.save()
        db.session.commit()

    return render_template("profile.html", user=current_user)
