import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pymongo import MongoClient

client = MongoClient(port=27017)
db = client.historical_data4


def get_coins(url):
    """this function get all coins list"""
    response = requests.get(url)
    coin_list = [i['id'] for i in response.json()]
    return coin_list


def get_csv(coin_id, end_date, start_date=20130428):
    """this function genrates will write into mongo
    db collections"""
    collection = db[coin_id]
    keys = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap']
    url = 'https://coinmarketcap.com/currencies/\
{0}/historical-data/?start={1}&end={2}'.format(coin_id, start_date, end_date)
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', attrs={'class': 'table'})
    list_of_rows = []
    for row in table.findAll('tr')[1:]:
        list_of_cells = []
        for cell in row.findAll('td'):
            list_of_cells.append(cell.text)
        list_of_rows.append(dict(zip(keys, list_of_cells)))
    collection.insert(list_of_rows)


current_date = datetime.today().strftime('%Y%m%d')
coins = get_coins('https://api.coinmarketcap.com/v1/ticker/?limit=10')
print ("there are %d coins..", len(coins))
for coin in coins:
    get_csv(coin, current_date)
print("Success all the coins data has been saved....")
