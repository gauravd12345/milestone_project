from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    TextAreaField,
    DateField,
    SelectField,
)
from wtforms.validators import DataRequired, Email, Length, Optional
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, DateField, IntegerField


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=255)])
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=128)]
    )
    submit = SubmitField("Create Account")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=255)])
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=128)]
    )
    submit = SubmitField("Log In")


class TaskForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Description")
    course_code = StringField("Course Code")
    status = SelectField(
        "Status",
        choices=[("open", "Open"), ("in_progress", "In Progress"), ("done", "Done")],
        default="open",
    )
    due_date = DateField("Due Date", format="%Y-%m-%d", validators=[Optional()])
    assignee_id = SelectField("Assignee", coerce=int)

    progress_note = TextAreaField(
        "Progress Update (optional)",
        render_kw={"rows": 3, "placeholder": "E.g., Finished sections 1–3; need to review examples."},
    )

    submit = SubmitField("Save")

class StudyGroupForm(FlaskForm):
    name = StringField(
        "Group Name",
        validators=[DataRequired(), Length(min=3, max=64)],
    )
    description = TextAreaField("Description")
    submit = SubmitField("Create Group")


class JoinGroupForm(FlaskForm):
    name = StringField(
        "Group Name",
        validators=[DataRequired(), Length(min=3, max=64)],
    )
    submit = SubmitField("Join Group")


class NudgeForm(FlaskForm):
    message = StringField("Message", validators=[Length(max=255)])
    submit = SubmitField("Send Nudge")


class LMSConnectForm(FlaskForm):
    canvas_url = StringField(
        "Canvas course URL",
        validators=[Optional(), Length(max=255)],
    )
    submit = SubmitField("Save LMS Settings")