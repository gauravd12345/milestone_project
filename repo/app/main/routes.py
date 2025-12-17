from datetime import date, timedelta
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from app import db
from app.models import Task
from app.forms import LMSConnectForm

main_bp = Blueprint("main", __name__, template_folder="templates")


@main_bp.route("/")
def index():
    # Public landing page – no login required here
    return render_template("main/index.html", title="StudyBuddy Home")


def _compute_activity(goals):
    """Return (streak_length, [ (label, count) ] for last 7 days)."""
    if not goals:
        return 0, []

    # dates where the user created goals
    created_dates = [g.created_at.date() for g in goals if g.created_at]
    date_set = set(created_dates)

    today = date.today()

    # current streak: consecutive days up to today with at least one goal created
    streak = 0
    d = today
    while d in date_set:
        streak += 1
        d = d - timedelta(days=1)

    # activity for the last 7 days
    activity = []
    for offset in range(6, -1, -1):  # 6 days ago -> today
        day = today - timedelta(days=offset)
        count = sum(1 for dt in created_dates if dt == day)
        label = day.strftime("%a")  # Mon, Tue, ...
        activity.append((label, count))

    return streak, activity


@main_bp.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    user = current_user

    goals = (
        Task.query.filter_by(assignee_id=user.id)
        .order_by(Task.created_at.desc())
        .all()
    )
    total = len(goals)
    completed = sum(1 for g in goals if g.status == "done")
    courses = sorted({g.course_code for g in goals if g.course_code})

    streak, activity = _compute_activity(goals)

    form = LMSConnectForm(obj=user)
    if form.validate_on_submit():
        url_val = (form.canvas_url.data or "").strip() or None
        user.canvas_url = url_val
        db.session.commit()
        flash("LMS settings updated.", "success")
        return redirect(url_for("main.profile"))

    return render_template(
        "profile.html",
        title="Profile",
        total=total,
        completed=completed,
        courses=courses,
        streak=streak,
        activity=activity,
        lms_form=form,
    )