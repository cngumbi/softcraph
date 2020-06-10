from datetime import datetime
from sqlalchemy.sql import func
from application import db, flask_bcrypt
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.declarative import declarative_base

#Base = declarative_base()
#create class user
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
    _password = db.Column('password', db.String(60), nullable=False)

    #date and time the account was created
    created_on = db.Column(db.DataTime, nullable=False, default=datetime.utcnow)
    
    """created_on = Column(DateTime(timezone=True), server_default=func.now())
    updated_on = Column(DateTime(timezone=True), onupdate=func.now())"""


    
    @hybrid_property
    def password(self):
        """The bcrypt'ed password of the given user"""
        return self._password


    @password.setter
    def password(self, password):
        """bcrypt the password on assignment"""
        self._password = flask_bcrypt.generate_password_hash(password)


    def __repr__(self):
        #return '<User {!r}>'.format(self.username)
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


    def is_authenticated(self):
        """All the registered user are authentified here"""
        return True


    def is_active(self):
        """all user are active"""
        return True

    
    def is_anonymous(self):
        """we do)::f):lf):'''user are authenticated"""
        return True


    def get_id(self):
        """Get user ID as a Unicode string"""
        return unicode(self.id)

    

