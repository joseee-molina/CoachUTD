from flask import Blueprint, redirect, url_for
from flask_login import current_user

index = Blueprint("index", __name__)


@index.get("/")
def root():
    if current_user.is_authenticated:
        return redirect(url_for("explore.feed"), code=301)
    else:
        return redirect(url_for("auth.login"))
