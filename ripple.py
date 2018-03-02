import hug
import requests 

@hug.get()
def ripple():
    request = requests.get('https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD')
    data = request.json()
    return data
