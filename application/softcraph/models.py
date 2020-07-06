from datetime import datetime
from sqlalchemy import Column, Integer, DateTime
from softcraph import db, login_manager
from flask_login import UserMixin

#load the users / user loader to find user by ID 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#create a class for User
class User(db.Model, UserMixin):
    #the primarykey of the users
    id = db.Column(db.Integer, primary_key = True)
    #unique usernames for each user
    username = db.Column(db.String(20), unique = True, nullable=False)
    #unique email for he users
    email = db.Column(db.String(120), unique = True, nullable=False)
    #image file for user profile
    image_file = db.Column(db.String(20), nullable=False, default='avatar.png')
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
