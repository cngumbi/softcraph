from flask import Flask, render_template, url_for
from addUser import AddUserForm, LoginForm
app = Flask(__name__)

#configer the secrect key
app.config['SECRET_KEY'] = "&\xfb?\xfbL\xd7\xc0z\x19ewF\xdd\xe6\xce(M\xbc\x15,"
@app.route("/")
@app.route("/home")
def softcraph():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='about')

@app.route("/AddUser")
def adduser():
    form = AddUserForm()
    return render_template('adduser.html', title='Add User', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('Login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)