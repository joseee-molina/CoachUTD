from flask import Blueprint, render_template, request, flash, url_for, redirect
from werkzeug.security import check_password_hash
from flask_login import current_user, login_user
from .models import User

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # login code goes here
        email = request.form.get("email")
        password = request.form.get("password", "")
        remember = True if request.form.get("remember") else False

        user = User.query.filter_by(email=email).first()

        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user or not check_password_hash(user.password, password):
            flash("Please check your login details and try again.")
            return redirect(
                url_for("auth.login"), code=403
            )  # if the user doesn't exist or password is wrong, reload the page

        # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember)
        # redirect to explore page
        return redirect(url_for("explore.feed"), code=200)

    return render_template("login.html", user=current_user)
