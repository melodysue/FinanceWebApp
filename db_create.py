from app import db
from models import BlogPost

#create the database and the db tables
db.create_all()

#insert
db.session.add(BlogPost("Nice", "Everything is nice."))
db.session.add(BlogPost("Great", "Everything is great."))

#commit the changes
db.session.commit()