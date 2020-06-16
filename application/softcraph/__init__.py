from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
#configer the secrect key
app.config['SECRET_KEY'] = "&\xfb?\xfbL\xd7\xc0z\x19ewF\xdd\xe6\xce(M\xbc\x15,"
#set the configaration of the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///softcraze.db'
#create a database instance
db = SQLAlchemy(app)
#the hash instance
bcrypt = Bcrypt(app)


from softcraph import routes

