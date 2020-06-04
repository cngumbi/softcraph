from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)

#configer the sql database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../softcraze.db'
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
flask_bcrypt = Bcrypt()

#local modules
from application.users import models as user_models
from application.users.views import users
#app.register_blueprint(users, url_prefix='/users')

#loading a user from the database
@login_manager.user_loader
def load_user(user_id):
    return application.user_models.query.get(int(user_id))
"""def contact():
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
"""
if __name__ == "__main__":
    app.run()