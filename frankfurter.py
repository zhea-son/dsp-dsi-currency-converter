import requests 
import pandas as pd
import matplotlib.pyplot as plt
from api import cc_get_all_currencies, cc_get_historical_trends

class Frankfurter():

    def __init__( self) :
        pass

    def get_available_currency( self ):
        dict_currencies = cc_get_all_currencies()
        list_currencies = list( dict_currencies.keys() )

        return list_currencies
    
    def get_last_years_trend( self, from_currency, to_currency ):
        
        rates_json = cc_get_historical_trends( from_currency, to_currency )

        df = pd.DataFrame.from_dict( rates_json["rates"], orient="index" )

        df = df.reset_index()
        df.columns = ["date", "rate"]

        df["date"] = pd.to_datetime( df["date"] )

        plt.figure(figsize=(8,4))
        plt.plot(df["date"], df["rate"], linestyle="-", color="blue")
        plt.title(f"Exchange Rate Over Three Years {from_currency} vs {to_currency}")
        plt.xlabel("Date")
        plt.ylabel("Rate")
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.tight_layout()
        plt.show()

        return plt