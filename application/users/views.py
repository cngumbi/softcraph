from flask import (Blueprint, flash, render_template, url_for, redirect, g)

from flask_login import login_user, logout_user, current_user

from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

#import local models
from models import User 
from application import flask_bcrypt


#setup he blueprint direction
users = Blueprint('users', __name__, template_folder='templates')

#create a login class
class LoginForm(Form):
    """
            represents the basic Login form elements & validators.
    """

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(),Length(min=16)])

    @users.rout('/login', methods=['GET', 'POST'])
    def login():
        """
        basic user login functionality

        we redirect the user to the default softcraze index.html if loged in

        we submited the user info if not loded in the call the validate_on_submit()
        to make sure the data matches

        """

    def current_user.is_authenticated():
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

    return render_template('users/login.html', form=form)


    @users.rout('/logout', methods=['GET'])
    def logout():
        lotout_user()
        return redirect(url_for(('softcraze.listing')))