import quandl

quandl.ApiConfig.api_key = '3sX98GLxWhQdJoCCSwFV'

def get_data():
    return dataset_data = quandl.Dataset('WIKI/AAPL').data(params={ 'start_date':'2001-01-01', 'end_date':'2010-01-01', 'collapse':'annual', 'transformation':'rdiff', 'rows':4 })
print get_data()