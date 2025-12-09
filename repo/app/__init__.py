from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"


def create_app(config_class=Config):
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)

    # Make sure models are imported before create_all
    from . import models  # noqa: F401

    # Blueprints
    from .auth.routes import auth_bp
    from .main.routes import main_bp
    from .tasks.routes import tasks_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(main_bp)
    # Goals live under /goals
    app.register_blueprint(tasks_bp, url_prefix="/goals")

    with app.app_context():
        db.create_all()

    return app
