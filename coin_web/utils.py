import requests


def get_coins(url):
    """this function get all coins list"""
    response = requests.get(url)
    coin_list = [i['id'] for i in response.json()]
    return coin_list
