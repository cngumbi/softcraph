from flask import Flask, render_template, url_for, flash, redirect
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

@app.route("/adduser",methods=['GET', 'POST'])
def adduser():
    form = AddUserForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success') 
        return redirect(url_for('adduser'))
    return render_template('adduser.html', title='Add User', form=form)


@app.route("/login",methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('softcraph'))
        else:
            flash('Login Unsuccessful. PLease check username and password', 'danger') 
    return render_template('Login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)