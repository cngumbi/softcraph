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
    #Favicons
    favics = os.path.join(app.config['UPLOAD_FOLDER'], 'favicon.png')
    apple_touch = os.path.join(app.config['UPLOAD_FOLDER'], 'apple-touch-icon.png')
    #setting the path tho the image files
    portF_1 =os.path.join(app.config['UPLOAD_FOLDER'], '1.jpg')
    portF_2 =os.path.join(app.config['UPLOAD_FOLDER'], '2.jpg')
    portF_3 =os.path.join(app.config['UPLOAD_FOLDER'], '3.jpg')
    portF_4 =os.path.join(app.config['UPLOAD_FOLDER'], '4.jpg')
    #client images
    client_1 =os.path.join(app.config['UPLOAD_FOLDER'], 'jwc.png')
    client_2 =os.path.join(app.config['UPLOAD_FOLDER'], 'dyt1.png')
    client_3 =os.path.join(app.config['UPLOAD_FOLDER'], 'client-1.png')
    client_4 =os.path.join(app.config['UPLOAD_FOLDER'], 'client-2.png')
    client_5 =os.path.join(app.config['UPLOAD_FOLDER'], 'client-3.png')
    client_6 =os.path.join(app.config['UPLOAD_FOLDER'], 'client-4.png')
    #quotes png
    quote_left =url_for('static', filename='img/quote-sign-left.png')
    quote_right =url_for('static', filename='img/quote-sign-right.png')
    #testimony png
    edith =url_for('static', filename='img/edith.png')
    dymetrian_tech =url_for('static', filename='img/dyt.png')
    #user_profile image
    image_file = url_for('static', filename='img/default.jpg')
    #about image
    image_files = url_for('static', filename='img/about_img.jpg')
    return render_template('index.html',
                                image_files=image_file, image_file1=image_files, portfolio_1=portF_1, portfolio_2=portF_2,
                                portfolio_3=portF_3, portfolio_4=portF_4, favicon=favics, apple=apple_touch,
                                quoteleft=quote_left, quoteright=quote_right, client2=client_2, client1=client_1, client3=client_3,
                                client4=client_4, client5=client_5, client6=client_6, testimony=edith, dymetrian=dymetrian_tech)


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
        return redirect(url_for('staff'))
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