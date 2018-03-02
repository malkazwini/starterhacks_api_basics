import hug
import requests 

@hug.get()
def litecoin():
    request = requests.get('https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD')
    data = request.json()
    return data
