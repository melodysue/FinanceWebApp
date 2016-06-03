from app import db
from models import BlogPost

# create the database and the db tables
db.create_all()

#insert
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Great", "I am beyond great"))
db.session.add(BlogPost("Life", "Life is so good"))

#commit the changes
db.session.commit()