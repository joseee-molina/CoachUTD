from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sqlalchemy import update
from .models import User
from . import db

profile = Blueprint("profile", __name__)


@profile.route("/profile/", methods=["GET", "POST"])
@login_required
def update_profile():
    user = current_user
    if request.method == "POST":
        # TODO: availability
        stmt = (
            update(User)
            .where(User.id == current_user.id)
            .values(
                {
                    "bio": request.values.get("bio"),
                    "coach": request.values.get("coach", type=bool),
                    "trainee": request.values.get("trainee", type=bool),
                    "mon": request.values.get("mon"),
                    "tue": request.values.get("tues"),
                    "wed": request.values.get("wed"),
                    "thu": request.values.get("thurs"),
                    "fri": request.values.get("fri"),
                    "sat": request.values.get("sat"),
                    "sun": request.values.get("sun"),
                }
            )
        )
        db.session.execute(stmt)
        return redirect(url_for("explore.feed"))

    return render_template("profile.html", current_user=user)
