import hug
import requests

@hug.get()
def bitcoin():
    request = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD')
    data = request.json()
    return data
