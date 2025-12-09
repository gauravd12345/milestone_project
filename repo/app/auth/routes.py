from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from ..forms import LoginForm, RegisterForm
from ..models import User
from .. import db

auth_bp = Blueprint("auth", __name__, template_folder="templates")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data.lower()
        existing = User.query.filter_by(email=email).first()
        if existing:
            flash("Email already registered.", "warning")
            return render_template("auth/register.html", form=form, title="Register")

        user = User(email=email)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Account created. Please log in.", "info")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", form=form, title="Register")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data.lower()
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_url = request.args.get("next") or url_for("main.index")
            flash("Welcome back!", "info")
            return redirect(next_url)
        flash("Invalid email or password.", "warning")

    return render_template("auth/login.html", form=form, title="Login")


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("main.index"))
