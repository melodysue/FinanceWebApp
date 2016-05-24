#for yahoo finance
import urllib as u
import string

def get_data(symbols):
    """
    input format: 'fb goog aapl scty'
    """
    symbols = symbols.split()
    data = []
    url = 'http://finance.yahoo.com/d/quotes.csv?s='
    for s in symbols:
        url += s+"+"
    url = url[0:-1]
    #url += "&f=sb3b2l1l"
    #url += "&f=sb2b3c6k2k1"
    url += "&f=sabl1l"
    print url
    f = u.urlopen(url,proxies = {})
    rows = f.readlines()
    for r in rows:
        values = [x for x in r.split(',')]
        symbol = values[0][1:-1]
        ask = float(values[1])
        bid = float(values[2])
        last = float(values[3])
        data.append([symbol,bid,ask,last,values[4]])
    return data

#symbols = 'fb goog aapl scty'
#print get_data(symbols)
