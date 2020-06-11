from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#create a registration class
class AddUserForm(FlaskForm):
    """to add a new user to the platform"""

    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    #email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=6, max=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Add User')

#create a login class
class LoginForm(FlaskForm):
    """
            represents the basic Login form elements & validators.
    """

    #email = StringField('Email', validators=[DataRequired() """, Email()"""])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=6, max=8)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')