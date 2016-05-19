# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session

# create the application object
app = Flask(__name__)

# LoginManager class
# login_manager = LoginManager()

#login_manager.init_app(app)

# provide callback used to reload the user object from the user ID stored in the session
#@login_manager.user_loader
#def load_user(user_id):
#    return User.get(user_id)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session["logged_in"] = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('logout')
def logout():
    session.pop('logged_in',None)
    return redirect(url_for('welcome'))

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
