from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email


class SignupForm(FlaskForm):
    username = StringField('Userame', validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    submit = SubmitField('Sign Up')
    email = StringField('Email address', validators=[DataRequired(), Email()])
    subscribe = SubmitField('subscribe')
