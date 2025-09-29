from datetime import date
import requests

class Currency:

    from_currency: str = None
    to_currency: str = None
    user_amount: float = 0
    rate: float = 0
    inverse_rate: float = 0
    user_date = date.today()
    
    def __init__(self, from_currency, to_currency, user_amount, user_date = date.today()):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.user_amount = user_amount
        self.user_date = user_date
        self.rate = self.get_rate
        self.inverse_rate = self.get_reverse_rate

    def check_validation(self):
        if self.from_currency == self.to_currency:
            return False
        elif self.user_date > date.today():
            return False
        else:
            return True

    def get_rate(self):
        url = f"https://api.frankfurter.dev/v1/{self.user_date}?base={self.from_currency}&symbols={self.to_currency}"
        
        response = requests.get(url)
        response_json = response.json()
        rate_value = response_json["rates"]
        self.rate = list(rate_value.values())[0]

        return self.rate
    
    def get_reverse_rate(self):
        self.inverse_rate = round(1 / self.rate, 5)

        return self.inverse_rate
    
    def get_converted_amount(self):
        rate = self.get_rate()
        return self.user_amount * rate
    
    def return_format_result(self):
        if self.check_validation():
            return f"The conversion rate on {self.user_date} from {self.from_currency} to {self.to_currency} was {self.get_rate()}. So {self.user_amount} in {self.from_currency} correspond to {self.get_converted_amount()} in {self.to_currency}. The inverse rate was {self.get_reverse_rate()}"
        else:
            return "Please enter valid information."

