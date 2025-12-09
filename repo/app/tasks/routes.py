from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    request,
)
from flask_login import login_required, current_user
from ..forms import TaskForm
from ..models import Task, User
from .. import db

tasks_bp = Blueprint("tasks", __name__, template_folder="templates")


@tasks_bp.route("/", methods=["GET"])
@login_required
def list_goals():
    goals = Task.query.order_by(Task.due_date.is_(None), Task.due_date).all()
    return render_template("tasks/list.html", tasks=goals, title="Your Goals")


@tasks_bp.route("/completed", methods=["GET"])
@login_required
def completed():
    goals = Task.query.filter_by(status="done").order_by(Task.due_date.desc()).all()
    return render_template("tasks/completed.html", tasks=goals, title="Completed Goals")


@tasks_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = TaskForm()

    # populate assignee choices
    users = User.query.order_by(User.email).all()
    form.assignee_id.choices = [(-1, "Unassigned")] + [(u.id, u.email) for u in users]

    if form.validate_on_submit():
        assignee_id = form.assignee_id.data if form.assignee_id.data != -1 else None

        goal = Task(
            title=form.title.data,
            description=form.description.data or "",
            course_code=form.course_code.data or None,
            status=form.status.data,
            due_date=form.due_date.data,
            assignee_id=assignee_id,
            # 🔹 actually save the progress update:
            progress_note=form.progress_note.data or "",
        )
        db.session.add(goal)
        db.session.commit()
        flash("Goal created.", "success")
        return redirect(url_for("tasks.list_goals"))

    return render_template("tasks/create.html", form=form, title="Create Goal")


@tasks_bp.route("/<int:task_id>/edit", methods=["GET", "POST"])
@login_required
def edit(task_id):
    goal = Task.query.get_or_404(task_id)

    form = TaskForm(obj=goal)

    users = User.query.order_by(User.email).all()
    form.assignee_id.choices = [(-1, "Unassigned")] + [(u.id, u.email) for u in users]

    if request.method == "GET":
        form.assignee_id.data = goal.assignee_id or -1

    if form.validate_on_submit():
        goal.title = form.title.data
        goal.description = form.description.data or ""
        goal.course_code = form.course_code.data or None
        goal.status = form.status.data
        goal.due_date = form.due_date.data
        goal.assignee_id = form.assignee_id.data if form.assignee_id.data != -1 else None
        # 🔹 update the progress note here:
        goal.progress_note = form.progress_note.data or ""

        db.session.commit()
        flash("Goal updated.", "success")
        return redirect(url_for("tasks.list_goals"))

    return render_template("tasks/edit.html", form=form, goal=goal, title="Edit Goal")



@tasks_bp.route("/<int:task_id>/delete", methods=["POST"])
@login_required
def delete(task_id):
    goal = Task.query.get_or_404(task_id)

    # Simple guard: you can’t delete someone else’s assigned goal
    if goal.assignee_id is not None and goal.assignee_id != current_user.id:
        flash("You can only delete your own goals or unassigned ones.", "warning")
        return redirect(url_for("tasks.list_goals"))

    db.session.delete(goal)
    db.session.commit()
    flash("Goal deleted.", "info")
    return redirect(url_for("tasks.list_goals"))

