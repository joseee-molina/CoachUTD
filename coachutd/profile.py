from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user
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
                    "coach": "coach" in request.values,
                    "trainee": "trainee" in request.values,
                    "mon": "mon" in request.values,
                    "tue": "tues" in request.values,
                    "wed": "wed" in request.values,
                    "thu": "thurs" in request.values,
                    "fri": "fri" in request.values,
                    "sat": "sat" in request.values,
                    "sun": "sun" in request.values,
                    "tennis": "tennis" in request.values,
                    "soccer": "soccer" in request.values,
                    "basketball": "basketball" in request.values,
                    "baseball": "baseball" in request.values,
                    "other_sport": "other_sport" in request.values,
                }
            )
        )
        db.session.execute(stmt)
        db.session.commit()

        return redirect(url_for("explore.feed"))

    return render_template("profile.html", current_user=user)
