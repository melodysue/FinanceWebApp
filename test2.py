import MySQLdb
from regex import *

db = MySQLdb.connect(host = "dallas146.arvixeshared.com",
                     db = "melodysu_database1",
                     user = "melodysu_msue",
                     passwd = "Melody88")

cur = db.cursor()

command = "SELECT FollowedTickers from melodysu_database1.Users WHERE Username = 'melodysue'"
    
cur.execute(command)
for row in cur.fetchall():
    x = row[0]

x = str(x)
data = get_data(x)
print data
