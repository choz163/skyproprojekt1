import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    """Конвертирует сумму из одной валюты в другую с помощью API данных о курсах валют."""

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"

    headers = {"apikey": API_KEY}

    response = requests.get(url, headers=headers)
    data = response.json()

    if data["success"]:
        return data["result"]
    else:
        raise ValueError(f"Error converting currency: {data['error']['info']}")
