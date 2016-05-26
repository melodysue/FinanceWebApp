import MySQLdb
from regex import *

def data():
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
    return data

def html_table(data):
    symbol = []
    ask = []
    bid = []
    last = []
    time = []
    for dataentry in data:
        symbol.append(dataentry[0])
        ask.append(dataentry[1])
        bid.append(dataentry[2])
        last.append(dataentry[3])
        time.append(dataentry[4])
    print '<tr>'
    for s in symbol:
        print '<td>'+s+'</td>'
    print '</tr>'
    print '<tr>'
    for a in ask:
        print '<td>'+a+'</td>'
    print '</tr>'
    print '<tr>'
    for b in bid:
        print '<td>'+b+'</td>'
    print '</tr>'
    print '<tr>'
    for l in last:
        print '<td>'+l+'</td>'
    print '</tr>'
    for t in time:
        print '<td>'+t[:7]+'</td>'
    print '</tr>'    

html_table(data())
heredata = data()
for dataentry in heredata:
    print dataentry