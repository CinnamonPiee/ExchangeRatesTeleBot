import os
from dotenv import load_dotenv, find_dotenv
from utils.get_flag import get_flag

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")
DEFAULT_CUR_DATA = [
    f'RUB {get_flag('RU')}',
    f'USD {get_flag('US')}',
    f'EUR {get_flag('EU')}',
    f'GBR {get_flag('GB')}',
    f'GEO {get_flag('GE')}'
]
ANOTHER_CUR_DATA = [
    f'KAZ {get_flag('KZ')}',
    f'UKR {get_flag('UA')}'
]