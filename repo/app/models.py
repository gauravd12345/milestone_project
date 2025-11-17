from . import db, login_manager
from flask_login import UserMixin

# Minimal User model for Flask-Login wiring
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=True)  # Not used in M1
    role = db.Column(db.String(50), default="student")

    def __repr__(self):
        return f"<User {self.email}>"

# One domain model stub (example: Course)
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(32), nullable=False)
    title = db.Column(db.String(255), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    # For M1, this can return None when no users exist; wiring is the key requirement.
    try:
        return User.query.get(int(user_id))
    except Exception:
        return None
