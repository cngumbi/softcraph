import datetime
from application import db

#create class user
class User(db.model):
    #the primarykey of the users
    id = db.Column(db.Integer, primarykey = True)

    #unique email for he users
    email = db.Column(db.String(255), unique = True)

    #unique usernames for each user
    username = db.Column(db.String(40), unique = True)

    #unique unse passwords
    password = db.Column(db.String(40))

    #date and time the account was created
    created_on = db.Column(db.DataTime, default = datetime.datetime.utcnow)

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