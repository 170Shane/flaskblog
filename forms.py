from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, email_validator


# Python classes will be translated to HTML forms

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('E-Mail', validators=[Email(), DataRequired(), Length(min=6, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=50)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),
                                                                     Length(min=6, max=50), EqualTo('password')])
    # also need a Submit button
    submit = SubmitField('Sign Up!')


class LoginForm(FlaskForm):
    email = StringField('E-Mail', validators=[Email(), DataRequired(), Length(min=6, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=50)])
    # include a Remember Me field
    remember_me = BooleanField('Remember Me?')
    # also need a Submit button
    submit = SubmitField('Sign Up!')
