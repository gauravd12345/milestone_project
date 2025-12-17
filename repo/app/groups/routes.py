from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

from app import db
from app.groups import groups_bp
from app.models import StudyGroup, GroupMembership, Nudge, User
from app.forms import StudyGroupForm, JoinGroupForm, NudgeForm


@groups_bp.route("/")
@login_required
def list_groups():
    """List all groups the current user belongs to."""
    memberships = GroupMembership.query.filter_by(user_id=current_user.id).all()
    groups = [m.group for m in memberships]
    return render_template("groups/list.html", groups=groups)


@groups_bp.route("/create", methods=["GET", "POST"])
@login_required
def create_group():
    form = StudyGroupForm()
    if form.validate_on_submit():
        name = form.name.data.strip()
        existing = StudyGroup.query.filter_by(name=name).first()
        if existing:
            flash("A group with that name already exists.", "danger")
            return redirect(url_for("groups.create_group"))

        group = StudyGroup(
            name=name,
            description=form.description.data.strip() if form.description.data else "",
            owner=current_user,
        )
        db.session.add(group)
        db.session.flush()  # get group.id

        membership = GroupMembership(user=current_user, group=group)
        db.session.add(membership)
        db.session.commit()

        flash("Study group created and you have been added as a member.", "success")
        return redirect(url_for("groups.view_group", group_id=group.id))

    return render_template("groups/create.html", form=form)


@groups_bp.route("/join", methods=["GET", "POST"])
@login_required
def join_group():
    form = JoinGroupForm()
    if form.validate_on_submit():
        name = form.name.data.strip()
        group = StudyGroup.query.filter_by(name=name).first()
        if not group:
            flash("No group with that name exists.", "danger")
            return redirect(url_for("groups.join_group"))

        existing_membership = GroupMembership.query.filter_by(
            user_id=current_user.id, group_id=group.id
        ).first()
        if existing_membership:
            flash("You are already a member of that group.", "info")
            return redirect(url_for("groups.view_group", group_id=group.id))

        membership = GroupMembership(user=current_user, group=group)
        db.session.add(membership)
        db.session.commit()

        flash(f"You joined {group.name}.", "success")
        return redirect(url_for("groups.view_group", group_id=group.id))

    return render_template("groups/join.html", form=form)


@groups_bp.route("/<int:group_id>", methods=["GET", "POST"])
@login_required
def view_group(group_id):
    group = StudyGroup.query.get_or_404(group_id)

    membership = GroupMembership.query.filter_by(
        user_id=current_user.id, group_id=group.id
    ).first()
    if not membership:
        flash("You are not a member of that group.", "danger")
        return redirect(url_for("groups.list_groups"))

    members = [m.user for m in group.memberships]

    nudge_form = NudgeForm()
    target_id = request.args.get("to", type=int)
    target_user = None
    if target_id and target_id in [u.id for u in members]:
        target_user = User.query.get(target_id)

    if nudge_form.validate_on_submit() and target_user:
        nudge = Nudge(
            sender=current_user,
            recipient=target_user,
            group=group,
            message=nudge_form.message.data.strip()
            if nudge_form.message.data
            else "",
        )
        db.session.add(nudge)
        db.session.commit()
        flash(f"You nudged {target_user.email}.", "success")
        return redirect(url_for("groups.view_group", group_id=group.id))

    recent_nudges = (
        Nudge.query.filter_by(group_id=group.id)
        .order_by(Nudge.created_at.desc())
        .limit(10)
        .all()
    )

    return render_template(
        "groups/detail.html",
        group=group,
        members=members,
        nudge_form=nudge_form,
        target_user=target_user,
        nudges=recent_nudges,
    )
