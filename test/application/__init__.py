from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

def create_app(config=None):
    app = Flask(__name__)

    if config is not None:
        app.config.form_object(config)
    #configer the sql database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../softcraze.db'
    #you can implimet os.urandom to generate the SECRET_KEY code()
    app.config['SECRET_KEY'] = "&\xfb?\xfbL\xd7\xc0z\x19ewF\xdd\xe6\xce(M\xbc\x15,"
    db = SQLAlchemy(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    flask_bcrypt = Bcrypt(app)

    return app




#local modules
from application.users import models as user_models
from application.users.views import users
app.register_blueprint(users, url_prefix='/users')

#db.init_app(app)

#loading a user from the database
@login_manager.user_loader
def load_user(user_id):
    return application.user_models.query.get(int(user_id))


def create_app():
    return db.create_all()
