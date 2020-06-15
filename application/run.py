from datetime import datetime 
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, DateTime
from addUser import AddUserForm, LoginForm

app = Flask(__name__)
#configer the secrect key
app.config['SECRET_KEY'] = "&\xfb?\xfbL\xd7\xc0z\x19ewF\xdd\xe6\xce(M\xbc\x15,"
#set the configaration of the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///softcraze.db'
#create a database instance
db = SQLAlchemy(app)


#create a class for User
class User(db.Model):
    #the primarykey of the users
    id = db.Column(db.Integer, primary_key = True)
    #unique usernames for each user
    username = db.Column(db.String(20), unique = True, nullable=False)
    #unique email for he users
    email = db.Column(db.String(120), unique = True, nullable=False)
    #image file for user profile
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    #unique user passwords
    #hash the password
    password = db.Column('password', db.String(60), nullable=False)
    #date and time the account was created
    created_on = db.Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    #create a relationship with the project model
    project = db.relationship('Project', backref='contributer', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

#create the project post
class Project(db.Model):
    #the primarykey of the project
    id = db.Column(db.Integer, primary_key = True)
    #title of the project
    title = db.Column(db.String(20), nullable=False)
    #create the date the project started
    created_on = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    #create the date the project was updated
    updated_on = Column(DateTime(timezone=True), nullable=True, default=datetime.utcnow)
    #advance the content later
    content = db.Column(db.Text, nullable=False)
    #create a user id to connect with the project
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Project('{self.title}', '{self.created_on}')"




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


if __name__ == '__main__':
    app.run(debug=True)