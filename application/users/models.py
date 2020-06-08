import datetime
from sqlalchemy.sql import func
from application import db, flask_bcrypt
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
#create class user
class User(db.Model):
    #the primarykey of the users
    id = Column(Integer, primary_key = True)

    #unique email for he users
    email = Column(db.String(255), unique = True, nullable=False)

    #unique usernames for each user
    username = Column(db.String(40), unique = True, nullable=False)

    #unique unse passwords
    #hash the password
    _password = Column('password', db.String(60))

    #date and time the account was created
    #created_on = Column(DataTime, default = datetime.datetime.utcnow)
    
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    updated_on = Column(DateTime(timezone=True), onupdate=func.now())


    
    @hybrid_property
    def password(self):
        """The bcrypt'ed password of the given user"""
        return self._password


    @password.setter
    def password(self, password):
        """bcrypt the password on assignment"""
        self._password = flask_bcrypt.generate_password_hash(password)


    def __repr__(self):
        return '<User {!r}>'.format(self.username)


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

    
    #initialize the database
   #db.create_all()
