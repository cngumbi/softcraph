from flask import render_template, url_for, flash, redirect

#custom libaries
from softcraph import app
from softcraph.addUser import AddUserForm, LoginForm
from softcraph.models import User, Project

@app.route("/")
@app.route("/home")
def softcraph():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='about')

@app.route("/adduser",methods=['GET', 'POST'])
def adduser():
    form = AddUserForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success') 
        return redirect(url_for('adduser'))
    return render_template('adduser.html', title='Add User', form=form)


@app.route("/login",methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('softcraph'))
        else:
            flash('Login Unsuccessful. PLease check username and password', 'danger') 
    return render_template('Login.html', title='Login', form=form)

