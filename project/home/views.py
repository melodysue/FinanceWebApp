#################
#### imports ####
#################

from project import db
from project.models import BlogPost, User
from flask import render_template, Blueprint
from flask_login import login_required
from flask_table import Table, Col


################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


################
#### routes ####
################

# use decorators to link the function to a url
@home_blueprint.route('/')
@login_required
def home():
    # return "Hello, World!"  # return a string
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)  # render a template


@home_blueprint.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')  # render a template


from regex import *
@home_blueprint.route('/watchlist')
@login_required
def watchlist():
    x = 'fb goog aapl scty'
    data = get_data(x)
    return render_template('watchlist.html', data=data)

@home_blueprint.route('/targeted-lead-list')
@login_required
def targeted():
    '''
    # Declare your table
    class ItemTable(Table):
        classes = ['table', 'table-striped']
        name = Col('Name')
        email = Col('Email')
        password = Col('password')

        # def tr_format(self, item):
        #     if item.title:
        #         return '<tr class="green">{}</tr>'
        #     else:
        #         return '<tr>{}</tr>'

    # Get some objects
    class Item(object):
        def __init__(self, name, email, password):
        #self.username = username
            self.name = name
            self.email = email
            self.password = password

    #items = [Item('Name1', 'Description1'),
    #         Item('Name2', 'Description2'),
    #         Item('Name3', 'Description3')]

    # Populate the table
    items = db.session.query(User).all()
    table = ItemTable(items)
    return render_template('targetedLeadList.html', table=table)
    '''
    return render_template('targetedLeadList.html')


