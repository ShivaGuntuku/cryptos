import requests
import csv
from datetime import datetime as d


request_data = requests.get(
    "https://api.coinmarketcap.com/v1/ticker/?convert=INR&limit=0")
request_json = request_data.json()


for curency in request_json:
    csv_file = curency['id'] + '_' + d.today().strftime('%d-%m-%Y')
    path = '{0}/{1}'.format('coins', csv_file)
    with open(path, 'a') as f:
        w = csv.DictWriter(f, curency.keys())
        if f.tell() == 0:
            w.writeheader()
            w.writerow(curency)
        else:
            w.writerow(curency)
    if curency['id'] == 'bitcoin':
        print (curency['price_inr'])
