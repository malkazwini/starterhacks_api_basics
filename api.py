import hug
import bitcoin
import ripple
import litecoin
import fakecoin


@hug.get('/')
def intro():
    return "Hi from CoinMaster"


@hug.extend_api()
def my_apis():
    return [bitcoin, litecoin, ripple, fakecoin]

