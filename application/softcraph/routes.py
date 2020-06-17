from flask import render_template, url_for, flash, redirect, request 
from flask_login import login_user, current_user, logout_user, login_required

#custom libaries
from softcraph import app, db, bcrypt
from softcraph.addUser import AddUserForm, LoginForm
from softcraph.models import User, Project


@app.route("/")
@app.route("/home")
def softcraph():
    return render_template('index.html')


@app.route("/staff")
def staff():
    return render_template('staff.html')


@app.route("/about")
def about():
    return render_template('about.html', title='about')

@app.route("/adduser",methods=['GET', 'POST'])
def adduser():
    form = AddUserForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success') 
        return redirect(url_for('login'))
    return render_template('adduser.html', title='Add User', form=form)


@app.route("/login",methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('staff'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('staff'))
        else:
            flash('Login Unsuccessful. PLease check email and password', 'danger') 
    return render_template('Login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')