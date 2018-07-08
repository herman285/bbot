import requests
from urllib.parse import urlencode, urljoin

class BinanceApi(object):

    def __init__(self, config):
        self.url = config.BASE_URL_V3
        self.public_url = config.PUBLIC_URL

    def __get(self, route, params=None):
        ret = requests.get(self.generate_path(route, params)).json()
        return ret

    def generate_path(self, route, params=None):
        return "%(url)s/%(route)s?%(params)s" % dict(url=self.url, route=route, params=urlencode(params))

    def get_price(self, symbol):
        route = '/ticker/price'
        params = dict(symbol=symbol)
        return self.__get(route, params)['price']

if __name__ == '__main__':
    from app.config import CONFIG

    bapi = BinanceApi(CONFIG)

    print(bapi.get_price('ETCBTC'))

