import requests 
import json
import numpy as np

class Frankfurter():

    def __init__(self):
        pass

    def get_available_currency(self):
        url = "https://api.frankfurter.dev/v1/currencies"

        currencies = requests.get(url)
        dict_currencies = currencies.json()
        list_currencies = list(dict_currencies.keys())

        return list_currencies
    
