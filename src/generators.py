import sys
from typing import Any, Generator


def filter_by_currency(transactions: list, currency_code: str = "USD") -> Generator[Any, Any, Any]:
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    # currency_code = (i for i in transactions if i ["operationsAmount "]["currency"]["code"])
    for transact in transactions:
        if transact.get("operationsAmount", {}).get("currency", {}).get("code", {}) == currency_code:
            yield transact


def transaction_descriptions(transactions: list) -> Generator[Any, Any, Any]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    if not transactions:
        sys.exit("Нет транзакций")
    for description_operation in transactions:
        yield description_operation.get("description")


def card_number_generator(start: int, stop: int) -> Generator[str, Any, None]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    for number in range(start, stop):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = "0" + card_number
        formatted_card_number = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
        yield formatted_card_number


for card_number in card_number_generator(1, 21):
    print(card_number)
