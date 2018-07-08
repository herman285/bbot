from app.config import CONFIG
from app.binance_api import BinanceApi


if __name__ == '__main__':


    bapi = BinanceApi(CONFIG)

    print(bapi.get_price('ETCBTC'))