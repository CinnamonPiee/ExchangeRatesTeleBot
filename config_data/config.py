import os
from dotenv import load_dotenv, find_dotenv
from utils.get_flag import get_flag
from utils.get_actual_currency import get_actual_currency

if not find_dotenv():
    exit("Environment variables are not loaded because the file is missing .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")
TWELVE_DATA = os.getenv("TWELVE_DATA_TOKEN")
DEFAULT_CUR_DATA = [
    f"RUB {get_flag("RU")}",
    f"USD {get_flag("US")}",
    f"EUR {get_flag("EU")}",
    f"GBP {get_flag("GB")}",
    f"GEL {get_flag("GE")}"
]
ANOTHER_CUR_DATA = [
    f"KAZ {get_flag("KZ")}",
    f"UKR {get_flag("UA")}"
]
CURRENCY_DATA = []
DATA_ACTUAL_CURRENCY = get_actual_currency()