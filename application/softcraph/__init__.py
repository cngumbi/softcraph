from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
#configer the secrect key
app.config['SECRET_KEY'] = "&\xfb?\xfbL\xd7\xc0z\x19ewF\xdd\xe6\xce(M\xbc\x15,"
#set the configaration of the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///softcraze.db'
#create a database instance
db = SQLAlchemy(app)
#the hash instance
bcrypt = Bcrypt(app)
#login instance
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info '


from softcraph import routes

