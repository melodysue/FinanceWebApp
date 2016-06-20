# import things
from flask_table import Table, Col
from project import db
from project.models import BlogPost

# Declare your table
class ItemTable(Table):
	name = Col('Name')
	description = Col('Description')

# Get some objects
class Item(object):
	def __init__(self, name, description):
		self.title = title
		self.description = description
		self.author = author

#items = [Item('Name1', 'Description1'),
#		 Item('Name2', 'Description2'),
#		 Item('Name3', 'Description3')]

items = db.session.query(BlogPost).all()

# Populate the table
table = ItemTable(items)