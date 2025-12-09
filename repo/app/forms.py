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
    title = StringField("Title", validators=[DataRequired(), Length(max=120)])
    description = TextAreaField("Description", validators=[Optional(), Length(max=2000)])
    due_date = DateField("Due date", validators=[Optional()], format="%Y-%m-%d")
    status = SelectField(
        "Status",
        choices=[
            ("open", "Open"),
            ("in_progress", "In Progress"),
            ("done", "Done"),
        ],
    )
    assignee_id = SelectField("Assignee", coerce=int, validators=[Optional()])
    course_code = StringField("Course", validators=[Optional(), Length(max=64)])
    submit = SubmitField("Save Goal")
