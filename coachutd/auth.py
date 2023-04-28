from flask import Blueprint, render_template, request, flash, url_for, redirect
from werkzeug.security import check_password_hash
from flask_login import current_user, login_user
from .models import User

auth = Blueprint("auth", __name__)


@auth.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # login code goes here
        username = request.form.get("username")
        password = request.form.get("password")
        remember = request.form.get("remember", default=False, type=bool)

        try:
            user = User.query.filter(User.username == username).one()
        except:
            flash("User not found")
            return (
                render_template("login.html"),
                403,
            )

        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if password and not check_password_hash(user.password, password):
            flash("Incorrect password")
            return (
                render_template("login.html"),
                403,
            )  # if the user doesn't exist or password is wrong, reload the page

        # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember)
        # redirect to explore page
        return redirect(url_for("explore.feed"))

    if current_user.is_authenticated:
        return redirect(url_for("explore.feed"))
    else:
        return render_template("login.html", user=current_user)
