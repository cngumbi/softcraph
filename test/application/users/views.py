from flask import (Blueprint, flash, render_template, url_for, redirect, g)

from flask_login import login_user, logout_user, current_user

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo #, Email

#import local models
#from models import User 
from application import flask_bcrypt


#setup he blueprint direction
users = Blueprint('users', __name__, template_folder='templates')

#create a registration class
class add_userForm(Form):
    """to add a new user to the platform"""

    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    #email = StringField('Email', validators=[DataRequired(), Email()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=16)])
    confirm_password = PasswordField('Confirm_Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Add User')


#create a login class
class LoginForm(Form):
    """
            represents the basic Login form elements & validators.
    """

    #email = StringField('Email', validators=[DataRequired() """, Email()"""])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=16)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

@users.route('/login', methods=['GET', 'POST'])
def login():
    """
    basic user login functionality
    we redirect the user to the default softcraze index.html if loged in
    we submited the user info if not loded in the call the validate_on_submit()
    to make sure the data matches
    """

    """
    if current_user.is_authenticated():
        return redirect(url_for('softcraze.listing'))


    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username).first()

        if not user:
            flash("NO such user exists")
            return render_template('users/login.html', form=form)

        if(not flask_bcrypt.check_password_hash(user.password, form.password.data)):
            flash("Invalid password")
            return render_template('users/login.html', form=form)

        login_user(user, remember=True)
        flash("Success! You're logged in.")
        return redirect(url_for("softcraze.listing"))
        """
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. PLease check username and password', 'danger')    
    return render_template('users/login.html', form=form)


@users.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for(('softcraze.listing')))


@users.route('/Add_user', methods=['GET', 'POST'])
def add_user():
    form = add_userForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success') 
        return redirect(url_for('add_user'))
    return render_template('users/add_user.html', form=form)