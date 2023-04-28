from flask import Blueprint, redirect, url_for
from flask_login import login_required

index = Blueprint("index", __name__)


@index.get("/")
@login_required
def root():
    return redirect(url_for("explore.feed"), code=301)
