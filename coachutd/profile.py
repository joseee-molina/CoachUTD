from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from .models import User
from . import db

profile = Blueprint("profile", __name__)


@profile.route("/profile", methods=["GET", "POST"])
@login_required
def update():
    user = current_user
    if request.method == "POST":
        # TODO: availability
        update = (
            User.update()
            .where(User.c.id == current_user.id)
            .values(
                {
                    "bio": request.values.get("bio"),
                    "age": request.values.get("age"),
                    "sex": request.values.get("sex"),
                    "coach": request.values.get("coach", type=bool),
                    "trainee": request.values.get("trainee", type=bool),
                }
            )
        )
        user = db.session.execute(update)

    return render_template("profile.html", current_user=user)
