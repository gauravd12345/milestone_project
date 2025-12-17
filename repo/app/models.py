from datetime import datetime, date
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager
from datetime import datetime
from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    # For StudyBuddy we mostly use "student", but could add "instructor" later
    role = db.Column(db.String(50), default="student")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # NEW: optional Canvas/LMS course URL
    canvas_url = db.Column(db.String(255), nullable=True)

    goals = db.relationship("Task", backref="assignee", lazy=True)

    # these relationships were already implied by your models:
    owned_groups = db.relationship(
        "StudyGroup",
        back_populates="owner",
        lazy=True,
    )
    group_memberships = db.relationship(
        "GroupMembership",
        back_populates="user",
        lazy=True,
    )
    sent_nudges = db.relationship(
        "Nudge",
        foreign_keys="Nudge.sender_id",
        back_populates="sender",
        lazy=True,
    )
    received_nudges = db.relationship(
        "Nudge",
        foreign_keys="Nudge.recipient_id",
        back_populates="recipient",
        lazy=True,
    )

    def set_password(self, raw: str) -> None:
        self.password_hash = generate_password_hash(raw)

    def check_password(self, raw: str) -> bool:
        return check_password_hash(self.password_hash, raw)

    def __repr__(self) -> str:
        return f"<User {self.email}>"


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, default="")
    status = db.Column(db.String(32), default="open")
    due_date = db.Column(db.Date, nullable=True)
    course_code = db.Column(db.String(64), nullable=True)
    assignee_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    progress_note = db.Column(db.Text, default="")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.status is None:
            self.status = "open"


class Course(db.Model):  # simple stub for future
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(32), nullable=False)
    title = db.Column(db.String(255), nullable=False)


class StudyGroup(db.Model):
    __tablename__ = "study_groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    owner = db.relationship("User", back_populates="owned_groups")

    memberships = db.relationship(
        "GroupMembership",
        back_populates="group",
        cascade="all, delete-orphan",
    )

    nudges = db.relationship(
        "Nudge",
        back_populates="group",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<StudyGroup {self.name}>"



class GroupMembership(db.Model):
    __tablename__ = "group_memberships"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey("study_groups.id"), nullable=False)

    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="group_memberships")
    group = db.relationship("StudyGroup", back_populates="memberships")

    __table_args__ = (
        db.UniqueConstraint("user_id", "group_id", name="uq_user_group"),
    )

    def __repr__(self):
        return f"<GroupMembership user={self.user_id} group={self.group_id}>"



class Nudge(db.Model):
    __tablename__ = "nudges"

    id = db.Column(db.Integer, primary_key=True)

    sender_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey("study_groups.id"), nullable=False)

    message = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    sender = db.relationship(
        "User", foreign_keys=[sender_id], back_populates="sent_nudges"
    )
    recipient = db.relationship(
        "User", foreign_keys=[recipient_id], back_populates="received_nudges"
    )
    group = db.relationship("StudyGroup", back_populates="nudges")

    def __repr__(self):
        return (
            f"<Nudge from={self.sender_id} to={self.recipient_id} "
            f"group={self.group_id}>"
        )



@login_manager.user_loader
def load_user(user_id: str):
    return User.query.get(int(user_id))
