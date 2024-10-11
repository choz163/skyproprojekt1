import json
import os

from src.external_api import convert_currency


def load_operations(path: str) -> list[dict]:
    """Загружает данные финансовых транзакций из файла JSON."""

    if not os.path.exists(path):
        return []

    try:
        with open(path, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        return []

    if not isinstance(data, list):
        return []

    return data


def get_transaction_rub(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях."""

    amount = transaction["amount"]
    currency = transaction["currency"]

    if currency == "RUB":
        return amount
    elif currency in ["USD", "EUR"]:
        return convert_currency(amount, currency, "RUB")
    else:
        raise ValueError(f"Unsupported currency: {currency}")
