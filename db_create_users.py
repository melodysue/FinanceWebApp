from app import db
from models import User

#insert data
db.session.add(User("Melody","msue16@cmc.edu","Melody88"))
db.session.add(User("Henry","thehenrysue@gmail.com","thisisme"))

#commit the changes
db.session.commit()