from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import current_user, login_required
from sqlalchemy import func
from .models import Post, Like, User
from . import db

explore = Blueprint("explore", __name__, url_prefix="/explore")


@explore.route("/", methods=["GET"])
@login_required
def feed():
    posts = (
        db.session.query(
            Post.created_at,
            Post.body,
            User.username.label("author"),
            User.coach.label("coach"),
            User.trainee.label("trainee"),
            func.count(Like.user).label("likes"),
            (func.count(Like.user).filter(Like.user == current_user.id) > 0).label(
                "liked"
            ),
        )
        .outerjoin(Like, Post.id == Like.post)
        .join(User, Post.author == User.id)
        .group_by(Post.id)
        .order_by(Post.created_at.desc())
        .all()
    )
    return render_template("explore.html", posts=posts)


@explore.route("/create/", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        body = request.values.get("body", "")
        if len(body.strip()) == 0:
            flash("Body is required!", "danger")
            return render_template("create_post.html"), 400

        post = Post(
            body=body,
            mon=request.values.get("mon") == "on",
            tue=request.values.get("tues") == "on",
            wed=request.values.get("wed") == "on",
            thu=request.values.get("thurs") == "on",
            fri=request.values.get("fri") == "on",
            sat=request.values.get("sat") == "on",
            sun=request.values.get("sun") == "on",
            author=current_user.id,
        )
        db.session.add(post)
        db.session.commit()

        return redirect(url_for("explore.feed"), code=303)

    return render_template("create_post.html")
