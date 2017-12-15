
import csv
from datetime import datetime as d
import requests
import time


currecy_list = ['bitcoin', 'ethereum',
                'ripple', 'litecoin']
notify_dict = {'bitcoin': 1, 'ethereum': 2,
               'ripple': 3, 'litecoin': 4}
final_val = {'bitcoin': 1, 'ethereum': 2,
             'ripple': 3, 'litecoin': 4}
per_dict = {'bitcoin': 1.27,
            'ethereum': 1.323,
            'ripple': 1.35,
            'litecoin': 1.32}

while True:
    print("running....")
    for currency in currecy_list:
        url = 'https://api.coinmarketcap.com/\
v1/ticker/{0}/?convert=INR'.format(currency)
        request = requests.get(url)
        request_json = request.json()
        for crypto in request_json:
            notify_dict[crypto['id']] = crypto['price_inr']
            mul = float(notify_dict[crypto['id']]) * per_dict[crypto['id']]
            final_val[crypto['id']] = mul
            csv_file = crypto['id'] + '_' + d.today().strftime('%d-%m-%Y')
            path = '{0}/{1}'.format('backed_crypto', csv_file)
            with open(path, 'a') as f:
                w = csv.DictWriter(f, crypto.keys())
                if f.tell() == 0:
                    w.writeheader()
                    w.writerow(crypto)
                else:
                    w.writerow(crypto)
    time.sleep(300)

