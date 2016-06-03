from app import db

class BlogPost(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Integer, nullable=False)
	description = db.Column(db.Integer, nullable=False)

	def __init__(self, title, description):
		self.title = title
		self.description = description

	def __repr__(self):
		return '<{}>'.format(self.title)
