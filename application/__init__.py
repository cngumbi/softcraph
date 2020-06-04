from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application import db
#from application.users.views import users

app = Flask(__name__)

#configer the sql database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../softcraze.db'
db = SQLAlchemy(app)
#app.register_blueprint(users, url_prefix='/users')

#local packages
#import application.models
def contact():
    return "my contacts"

#create route to handle login
@app.route('/login', methods =['GET', 'POST'])
def login():
    if request.methods == 'POST':
        #logic to handle login
        pass
    else:
        #display login form
        pass
"""
if __name__ == "__main__":
    app.run()