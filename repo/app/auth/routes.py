from flask import Blueprint, render_template, redirect, url_for, flash, request
from ..forms import LoginForm

auth_bp = Blueprint("auth", __name__, template_folder="templates")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            flash("Not implemented: authentication flow will arrive in M2.", "info")
            return redirect(url_for("main.index"))
        else:
            flash("Please correct the errors below.", "warning")
    return render_template("auth/login.html", form=form, title="Login")
