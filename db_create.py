from project import db
from project.models import BlogPost

# create the database and the db tables
db.create_all()

#insert
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Great", "I am beyond great"))
db.session.add(BlogPost("Life", "Life is so good"))
db.session.add(BlogPost("newpost", "setting up local postgres"))

#commit the changes
db.session.commit()