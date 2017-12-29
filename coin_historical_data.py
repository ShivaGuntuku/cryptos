import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_coins(url):
    """this function get all coins list"""
    response = requests.get(url)
    coin_list = [i['id'] for i in response.json()]
    return coin_list


def date_formating(date_string):
    """this function is used for formating the date
    Dec 21, 2017 to 21-Dec-2017"""
    s1 = date_string.split(', ')[0].split(' ')
    s1.append(date_string.split(', ')[1])
    s1[0], s1[1] = s1[1], s1[0]
    return '-'.join(s1)


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
        list_of_cells[0] = date_formating(list_of_cells[0])
        list_of_rows.append(list_of_cells)
    file_name = '{0}/{1}.csv'.format('historical_data', coin_id)
    with open(file_name, 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['date', 'open', 'high', 'low',
                         'close', 'volume', 'market cap'])
        writer.writerows(list_of_rows)


current_date = datetime.today().strftime('%Y%m%d')
coins = get_coins('https://api.coinmarketcap.com/v1/ticker/?limit=10')
print ("there are coins..", len(coins))
for coin in coins:
    get_csv(coin, current_date)
print("Success all the coins data has been saved....")
