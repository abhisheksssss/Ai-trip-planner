import requests


class CurrencyConverter:
    def __init__(self):
        self.base_url=f"https://v.exchangerate-api.com/v6/{api_key}/latest/"
        
    def convert(self,amount:float,from_currecy:str,to_currency:str):
        """Convert the amount from one currecy to another"""
        url=f"{self.base_url}/{from_currecy}"
        response=requests.get(url)
        if response.status_code!=200:
            raise Exception("Api call failed",response.json())
        rates=response.json()["conversion_rates"]
        if to_currency not in rates:
            raise ValueError(f"{to_currency} not founded in exchange rates.")
        return amount*rates[to_currency]