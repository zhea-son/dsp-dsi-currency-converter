import requests
from datetime import date
from dateutil.relativedelta import relativedelta

# API call through the url
def cc_api_call( url ):
    response = requests.get(url)
    return response.json()

# Get exchange rate from the API
def cc_get_exchange_rate( exchange_date, from_currency, to_currency ):
    url = f"https://api.frankfurter.dev/v1/{exchange_date}?base={from_currency}&symbols={to_currency}"
        
    response = cc_api_call( url )
    return response

# Get all currencies from the API
def cc_get_all_currencies():
    url = "https://api.frankfurter.dev/v1/currencies"

    response = cc_api_call( url )
    return response

# Get rate trend through last three years
def cc_get_historical_trends( from_currency, to_currency ):
    today_date = date.today()
    three_years_ago = today_date - relativedelta(years=3)
    url = f"https://api.frankfurter.dev/v1/{three_years_ago}..?base={from_currency}&symbols={to_currency}"

    response = cc_api_call( url )
    return response