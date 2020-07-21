from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField ,SubmitField
from wtforms.validators import DataRequired, Email , EqualTo, Length
from wtforms import ValidationError

from flask_login import current_user
from models import User


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    fname = StringField('First Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('pass_confirm', message='Passwords must match'), Length(min = 8, max=16)])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('The email you chose has already been registered')
    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('The username yuo chose has already been registered')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')


class MakeTeamForm(FlaskForm):
    team_name = StringField('Team Name', validators=[DataRequired()])
    team_password = PasswordField('Password', validators=[DataRequired(),EqualTo('pass_confirm', message='Passwords must match'), Length(min = 8, max=16)])
    team_pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Make Team')


class TeamLoginForm(FlaskForm):
    team_name = StringField('Team Name', validators=[DataRequired()])
    team_password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enter Team')
