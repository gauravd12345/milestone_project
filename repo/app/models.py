from datetime import datetime, date
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    # For StudyBuddy we mostly use "student", but could add "instructor" later
    role = db.Column(db.String(50), default="student")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    goals = db.relationship("Task", backref="assignee", lazy=True)

    def set_password(self, raw: str) -> None:
        self.password_hash = generate_password_hash(raw)

    def check_password(self, raw: str) -> bool:
        return check_password_hash(self.password_hash, raw)

    def __repr__(self) -> str:
        return f"<User {self.email}>"


class Task(db.Model):
    """In code we call it Task, in UI we present it as a 'goal'."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, default="")
    status = db.Column(db.String(32), default="open")  # open, in_progress, done
    due_date = db.Column(db.Date, nullable=True)

    # StudyBuddy: optional course tag like "CS101"
    course_code = db.Column(db.String(64), nullable=True)

    assignee_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Course(db.Model):  # simple stub for future
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(32), nullable=False)
    title = db.Column(db.String(255), nullable=False)


@login_manager.user_loader
def load_user(user_id: str):
    return User.query.get(int(user_id))
