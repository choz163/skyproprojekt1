import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def convert_currency(transaction: dict) -> float:
    """Конвертирует сумму из одной валюты в другую с помощью API данных о курсах валют."""

    amount = transaction["amount"]
    from_currency = transaction["currency"]
    to_currency = "RUB"

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
    headers = {"apikey": API_KEY}

    response = requests.get(url, headers=headers)
    data = response.json()

    if data.get("success"):
        return data["result"]
    else:
        raise ValueError(f"Ошибка конвертации валюты: {data.get('error', {}).get('info', 'Unknown error')}")
