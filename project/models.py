from project import db
from project import bcrypt 

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class BlogPost(db.Model):

	__tablename__ = "posts"

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, nullable=False)
	description = db.Column(db.String, nullable=False)
	author_id = db.Column(db.Integer, ForeignKey('users.id'))

	def __init__(self, title, description):
		self.title = title
		self.description = description

	def __repr__(self):
		return '<{}>'.format(self.title)


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    #username = db.Column(db.String, nullable=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    posts = relationship("BlogPost", backref="author")

    def __init__(self, name, email, password):
        #self.username = username
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)
        
    def __repr__(self):
        return '<name {}'.format(self.name)

'''
class Following(db.Model):

    __tablename__ = "followed_tickers"

    author_id = db.Column(db.Integer, primary_key=True, ForeignKey('users.id'))
    ticker_id = db.Column(db.Integer, primary_key=True, ForeignKey('tickers.id'))

    def __init__(self):
        self = self

    def __repr__(self):
        return '<{}>'

class Ticker(db.Model):

    __tablename__ = "tickers"

    ticker_id = db.Column(db.Integer, primary_key=True)
    ticker_symbol = db.Column(db.String, nullable=False)
    company = db.Column(db.String, nullable=False)

    def __init__(self, ticker_symbol, company):
        self.ticker_symbol = ticker_symbol
        self.company = company
    def __repr__(self):
        return '<{}>'.format(self.ticker_symbol)

'''