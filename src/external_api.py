import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def convert_currency(transaction: dict) -> float:
    """Конвертирует сумму из одной валюты в другую с помощью API данных о курсах валют."""

    amount = transaction["operationAmount"]["amount"]
    from_currency = transaction["operationAmount"]["currency"]["code"]
    to_currency = "RUB"

    if from_currency == to_currency:
        return float(amount)

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
    headers = {"apikey": API_KEY}

    response = requests.get(url, headers=headers)
    data = response.json()

    if data.get("success"):
        return float(data["result"])
    else:
        raise ValueError(f"Ошибка конвертации валюты: {data.get('error', {}).get('info', 'Unknown error')}")


# transaction = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}
#
# converted_amount = convert_currency(transaction)
# print(converted_amount)
