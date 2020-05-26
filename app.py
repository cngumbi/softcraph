from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello world"

#create the contact route to handle contacts
@app.route('/contact')
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

if __name__ == "__main__":
    app.run()