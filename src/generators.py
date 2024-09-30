import sys

from typing import Any, Generator


def filter_by_currency(transactions: list, currency_code: str = "USD") -> Generator[Any, Any, Any]:
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    # currency_code = (i for i in transactions if i ["operationsAmount "]["currency"]["code"])
    if transactions == []:
        sys.exit("Нет транзакций")
    for i in transactions:
        if i.get("operationAmount").get("currency").get("code") != currency_code:
            sys.exit("В транзакциях нет такого кода")
        elif i.get("operationAmount").get("currency").get("code") == currency_code:
            yield i


def transaction_descriptions(transactions: list) -> Generator[Any, Any, Any]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    if not transactions:
        sys.exit("Нет транзакций")
    for desc_operation in transactions:
        yield desc_operation.get("description")


def card_number_generator(start: int, stop: int) -> Generator[str, Any, None]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    for x in range(start, stop + 1):
        number_zero = "0000000000000000"
        card_number = number_zero[: -len(str(x))] + str(x)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
