from flask import Blueprint, render_template
from flask_login import current_user, login_required
from ..models import Task

main_bp = Blueprint("main", __name__, template_folder="templates")


@main_bp.route("/")
def index():
    # Public landing page – no login required here
    return render_template("main/index.html", title="StudyBuddy Home")


@main_bp.route("/profile")
@login_required
def profile():
    goals = Task.query.filter(
        (Task.assignee_id == current_user.id) | (Task.assignee_id.is_(None))
    ).all()
    total = len(goals)
    completed = len([g for g in goals if g.status == "done"])
    courses = sorted({g.course_code for g in goals if g.course_code})

    return render_template(
        "main/profile.html",
        goals=goals,
        total=total,
        completed=completed,
        courses=courses,
        title="Profile",
    )
