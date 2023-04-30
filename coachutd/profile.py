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
                    "mon": request.values.has_key("mon"),
                    "tue": request.values.has_key("tues"),
                    "wed": request.values.has_key("wed"),
                    "thu": request.values.has_key("thurs"),
                    "fri": request.values.has_key("fri"),
                    "sat": request.values.has_key("sat"),
                    "sun": request.values.has_key("sun"),
                    "tennis": request.values.get("tennis", type=bool),
                    "soccer": request.values.get("soccer", type=bool),
                    "basketball": request.values.get("basketball", type=bool),
                    "baseball": request.values.get("baseball", type=bool),
                    "other_sport": request.values.get("other_sport", type=bool),
                }
            )
        )
        db.session.execute(stmt)
        return redirect(url_for("explore.feed"))

    return render_template("profile.html", current_user=user)
