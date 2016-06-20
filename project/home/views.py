#################
#### imports ####
#################

from project import db
from project.models import BlogPost
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
def welcome():
    return render_template('welcome.html')  # render a template

@home_blueprint.route('/targeted-lead-list')
def targeted():
    # Declare your table
    class ItemTable(Table):
        title = Col('Title')
        description = Col('Description')

    # Get some objects
    class Item(object):
        def __init__(self, title, description):
            self.title = title
            self.description = description

    items = [Item('Name1', 'Description1'),
             Item('Name2', 'Description2'),
             Item('Name3', 'Description3')]

    # Populate the table
    table = ItemTable(items)
    return render_template('targetedLeadList.html', table=table)


