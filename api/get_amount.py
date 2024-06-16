import requests
from config_data.config import TWELVE_DATA


API_KEY = TWELVE_DATA
BASE_URL = f"https://api.twelvedata.com"


def get_amount(first_rate, second_rate, count_money):
    try:
        req = requests.get(f"{BASE_URL}/currency_conversion", params={
            "symbol": f"{first_rate}/{second_rate}",
            "amount": count_money,
            "apikey": API_KEY
        
        })
        response = req.json()
        return response["amount"]
    except KeyError:
        return f"Sorry, the bot does not yet have this pair of currencies '{first_rate}/{second_rate}', but we are working on it."

