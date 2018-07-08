import configparser

config_parser = configparser.ConfigParser()
config_parser.read('config.ini')

API_KEY = config_parser['KEYS']['API_KEY']
SECRET_KEY = config_parser['KEYS']['API_KEY']