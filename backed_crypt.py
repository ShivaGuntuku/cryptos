import requests
import csv
from datetime import datetime as d

currecy_list = ['bitcoin', 'ethereum',
                'ripple', 'litecoin']
for currency in currecy_list:
    url = 'https://api.coinmarketcap.com/\
v1/ticker/{0}/?convert=INR'.format(currency)
    request = requests.get(url)
    request_json = request.json()
    for crypto in request_json:
        csv_file = crypto['id'] + '_' + d.today().strftime('%d-%m-%Y')
        path = '{0}/{1}'.format('backed_crypto', csv_file)
        with open(path, 'a') as f:
            w = csv.DictWriter(f, crypto.keys())
            if f.tell() == 0:
                w.writeheader()
                w.writerow(crypto)
            else:
                w.writerow(crypto)
