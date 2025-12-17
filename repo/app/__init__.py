# app/__init__.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message_category = "info"  # shows as 'info' flash


def create_app(config_class=Config):
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)

    # Import models so they are registered
    from . import models  # noqa: F401

    # Blueprints
    from .auth.routes import auth_bp
    from .main.routes import main_bp
    from .tasks.routes import tasks_bp
    from .groups.routes import groups_bp   # <-- NEW

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(main_bp)
    app.register_blueprint(tasks_bp, url_prefix="/goals")
    app.register_blueprint(groups_bp, url_prefix="/groups")  # <-- NEW

    # Error handlers for nicer edge-case behavior
    @app.errorhandler(404)
    def not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def internal_error(error):
        # db.session.rollback()  # optional if you use transactions heavily
        return render_template("errors/500.html"), 500

    with app.app_context():
        db.create_all()

    return app
