# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from functools import wraps
#import sqlite3
import MySQLdb

# create the application object
app = Flask(__name__)
bcrypt = Bcrypt(app)

#config
app.config.from_object('config.BaseConfig')
#import os
#app.config.from_object(os.environ["APP_SETTINGS"])

#app.secret_key = "this_is_the_secret_key"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

#create the sqlalchemy object
#db = SQLAlchemy(app)

#create the mySQL object
db = MySQLdb.connect(host = "dallas146.arvixeshared.com",
                     db = "melodysu_database1",
                     user = "melodysu_msue",
                     passwd = "Melody88")

cur = db.cursor()

username = ""
#from models import *
from regex import *

# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

# use decorators to link the function to a url
@app.route('/')
@login_required
def home():
    # return "Hello, World!"  # return a string
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)  # render a template

@app.route('/watchlist')
@login_required
def watchlist():

    #posts = db.session.query(BlogPost).all()
    global username

    command = "SELECT FollowedTickers from melodysu_database1.Users WHERE Username = '" + username + "'"
    #flash(command1)
    #command = "SELECT FollowedTickers from melodysu_database1.Users WHERE Username = 'melodysue'"

    cur.execute(command)
    for row in cur.fetchall():
        x = row[0]
    x = str(x)
    data = get_data(x)

    return render_template('watchlist.html', data = data)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        global username
        username = request.form['username']
        password = request.form['password']
        command = "Select Count(*) from melodysu_database1.Users where Username='" + username + "' and Password= '" + password + "'"
        #command = "Select * From 'Users' where 1"
        cur.execute(command)

        for row in cur.fetchall():
            x = row[0]
        if x == 1:
            session["logged_in"] = True
            flash('You were just logged in!')
            return redirect(url_for('watchlist'))
        else:
            error = "Invalid credentials. Please try again."
        """
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'

        else:
            session["logged_in"] = True
            flash('You were just logged in!')
            return redirect(url_for('watchlist'))
        """
        
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in',None)
    flash('You were just logged out!')
    return redirect(url_for('welcome'))



#def connect_db():
#    return sqlite3.connect(app.database)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run()
