from project import db
from project.models import User

#insert data
#db.session.add(User("Melody","msue16@cmc.edu","Melody88"))
#db.session.add(User("Henry","thehenrysue@gmail.com","thisisme"))
db.session.add(User("admin","ad@min.com","admin"))

#commit the changes
db.session.commit()