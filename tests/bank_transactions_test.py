import src.bank_transactions


def test_find_transactions_by_description():
    transactions = [
        {"date": "08.12.2019", "description": "Открытие вклада", "amount": "40542 руб."},
        {"date": "12.11.2019", "description": "Перевод с карты на карту", "amount": "130 USD"},
        {"date": "18.07.2018", "description": "Перевод организации", "amount": "8390 руб."},
        {"date": "03.06.2018", "description": "Перевод со счета на счет", "amount": "8200 EUR"},
    ]

    # Поиск по слову "Перевод"
    result = src.bank_transactions.find_transactions_by_description(transactions, "Перевод")
    assert len(result) == 3
    assert {"date": "12.11.2019", "description": "Перевод с карты на карту", "amount": "130 USD"} in result
    assert {"date": "18.07.2018", "description": "Перевод организации", "amount": "8390 руб."} in result
    assert {"date": "03.06.2018", "description": "Перевод со счета на счет", "amount": "8200 EUR"} in result


def test_count_transactions_by_category():
    transactions = [
        {"date": "08.12.2019", "description": "Открытие вклада", "amount": "40542 руб."},
        {"date": "12.11.2019", "description": "Перевод с карты на карту", "amount": "130 USD"},
        {"date": "18.07.2018", "description": "Перевод организации", "amount": "8390 руб."},
        {"date": "03.06.2018", "description": "Перевод со счета на счет", "amount": "8200 EUR"},
    ]

    result = src.bank_transactions.count_transactions_by_category(transactions)
    assert len(result) == 2
    assert result["Открытие"] == 1
    assert result["Перевод"] == 3
