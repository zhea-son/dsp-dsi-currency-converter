import requests 
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from dateutil.relativedelta import relativedelta

class Frankfurter():

    def __init__(self):
        pass

    def get_available_currency(self):
        url = "https://api.frankfurter.dev/v1/currencies"

        currencies = requests.get(url)
        dict_currencies = currencies.json()
        list_currencies = list(dict_currencies.keys())

        return list_currencies
    
    def get_last_years_trend(self, from_currency, to_currency):
        today_date = date.today()
        three_years_ago = today_date - relativedelta(years=3)
        url = f"https://api.frankfurter.dev/v1/{three_years_ago}..?base={from_currency}&symbols={to_currency}"

        rates = requests.get(url)
        rates_json = rates.json()

        df = pd.DataFrame.from_dict(rates_json["rates"], orient="index")

        df = df.reset_index()
        df.columns = ["date", "rate"]

        df["date"] = pd.to_datetime(df["date"])

        plt.figure(figsize=(8,4))
        plt.plot(df["date"], df["rate"], linestyle="-", color="blue")
        plt.title(f"Exchange Rate Over Three Years {from_currency} vs {to_currency}")
        plt.xlabel("Date")
        plt.ylabel("Rate")
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.tight_layout()
        plt.show()

        return plt