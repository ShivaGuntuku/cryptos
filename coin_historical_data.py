import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_coins(url):
    """this function get all coins list"""
    response = requests.get(url)
    coin_list = [i['id'] for i in response.json()]
    return coin_list


def get_csv(coin_id, end_date, start_date=20130428):
    """this function genrates the csv file"""
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
        list_of_rows.append(list_of_cells)
    file_name = '{0}/{1}.csv'.format('historical_data', coin_id)
    with open(file_name, 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Date', 'Open', 'High', 'Low',
                         'Close', 'Volume', 'Market Cap'])
        writer.writerows(list_of_rows)


current_date = datetime.today().strftime('%Y%m%d')
coins = get_coins('https://api.coinmarketcap.com/v1/ticker/?limit=1')
print ("there are %d coins..", len(coins))
for coin in coins:
    get_csv(coin,current_date,20171201)
print("Success all the coins data has been saved....")
