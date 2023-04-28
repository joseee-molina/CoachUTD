from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    db.init_app(app)

    # create tables
    with app.app_context():
        from . import models as _

        db.create_all()

    # if in development mode, seed the tables with sample data
    if app.debug:
        from .seed_sample import seed

        with app.app_context():
            seed(db.session)

    # set up login with flask-login
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from .models import User

    login_manager.user_loader(lambda user_id: db.session.get(User, user_id))

    # register controllers
    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    from .profile import profile as profile_blueprint

    app.register_blueprint(profile_blueprint)

    from .explore import explore as explore_blueprint

    app.register_blueprint(explore_blueprint)

    from .index import index as index_blueprint

    app.register_blueprint(index_blueprint)

    return app
