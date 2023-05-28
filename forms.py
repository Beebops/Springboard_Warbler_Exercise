from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    InputRequired,
    EqualTo,
    ValidationError,
)
from flask import g


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField("text", validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField("Username", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[Length(min=6)])
    image_url = StringField("(Optional) Image URL")


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[Length(min=6)])


class EditUserProfileForm(FlaskForm):
    """Edit User Profile form."""

    username = StringField("Username", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    # password = PasswordField("Password", validators=[Length(min=6)])
    image_url = StringField("Add your profile pic")
    header_image_url = StringField("Add a header pic")
    bio = StringField("Introduce yourself")
    current_password = PasswordField("Current Password", validators=[DataRequired()])
