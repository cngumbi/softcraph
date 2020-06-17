from flask import render_template, url_for, flash, redirect, request 
from flask_login import login_user, current_user, logout_user, login_required
import os
#custom libaries
from softcraph import app, db, bcrypt
from softcraph.addUser import AddUserForm, LoginForm
from softcraph.models import User, Project


@app.route("/")
@app.route("/home")
def softcraph():
    #setting the path tho the image files
    portF_1 =os.path.join(app.config['UPLOAD_FOLDER'], '1.jpg')
    portF_2 =os.path.join(app.config['UPLOAD_FOLDER'], '2.jpg')
    portF_3 =os.path.join(app.config['UPLOAD_FOLDER'], '3.jpg')
    portF_4 =os.path.join(app.config['UPLOAD_FOLDER'], '4.jpg')
    #client images
    client_1 =os.path.join(app.config['UPLOAD_FOLDER'], 'jwc.png')
    client_2 =os.path.join(app.config['UPLOAD_FOLDER'], 'dyt.png')
    #testimonials
    testimonial =os.path.join(app.config['UPLOAD_FOLDER'], 'EdithMweruNduritu.jpeg')
    #user_profile image
    image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template('index.html', image_files=image_file, portfolio_1=portF_1, portfolio_2=portF_2,
                                portfolio_3=portF_3, portfolio_4=portF_4, client1=client_1, client2=client_2, 
                                testimony=testimonial)


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