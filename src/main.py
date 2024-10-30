import os
from pathlib import Path
from typing import Any, Dict, List

from src.bank_transactions import find_transactions_by_description
from src.decorators import log
from src.external_api import convert_currency
from src.generators import filter_by_currency
from src.masks import get_mask_account
from src.processing import filter_by_state, sort_by_date
from src.reading_operations import read_csv, read_excel
from src.utils import load_operations
from src.widget import mask_account_card


@log()
def main() -> None:
    """Основная функция для работы с банковскими транзакциями."""

    # Приветствие пользователя
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Пути к файлам (относительные пути)
    json_file_path: Path = Path("../data/operations.json")
    csv_file_path: Path = Path("../data/transactions.csv")
    excel_file_path: Path = Path("../data/transactions_excel.xlsx")

    # Выбор файла
    while True:
        file_type: str = input("Выберите тип файла для загрузки (1 - JSON, 2 - CSV, 3 - XLSX): ")

        if file_type == "1":
            if json_file_path.is_file():
                transactions: List[Dict[str, Any]] = load_operations(json_file_path)
                break
            else:
                print("JSON файл не найден.")
        elif file_type == "2":
            if csv_file_path.is_file():
                transactions: List[Dict[str, Any]] = read_csv(csv_file_path)
                break
            else:
                print("CSV файл не найден.")
        elif file_type == "3":
            if excel_file_path.is_file():
                transactions: List[Dict[str, Any]] = read_excel(excel_file_path)
                break
            else:
                print("XLSX файл не найден.")
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

    # Фильтрация по статусу
    while True:
        status: str = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. "
            "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        )
        status = status.upper()
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        else:
            print('Статус операции "{}" недоступен.'.format(status))

    transactions = filter_by_state(transactions, status)
    print('Операции отфильтрованы по статусу "{}"'.format(status))

    # Сортировка по дате
    sort_by_date_input: str = input("Отсортировать операции по дате? Да/Нет\n").lower()
    if sort_by_date_input == "да":
        sort_order_input: str = input(
            "Отсортировать по возрастанию или по убыванию? (введите 'возрастанию' или 'убыванию')\n"
        ).lower()
        sort_order: bool = True if sort_order_input == "возрастанию" else False
        transactions = sort_by_date(transactions, sort_order)

    # Фильтрация по рублевым транзакциям
    filter_by_rub_input: str = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
    if filter_by_rub_input == "да":
        transactions = filter_by_currency(transactions, "руб.")

    # Фильтрация по слову в описании
    filter_by_description_input: str = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"
    ).lower()
    if filter_by_description_input == "да":
        search_string: str = input("Введите слово для поиска: ")
        transactions = find_transactions_by_description(transactions, search_string)

    # Печать результата
    print("Распечатываю итоговый список транзакций...")
    print("Всего банковских операций в выборке: {}".format(len(transactions)))
    for transaction in transactions:
        if "operationAmount" in transaction:
            amount = transaction["operationAmount"]["amount"]
            currency = transaction["operationAmount"]["currency"]["name"]
            date = transaction["date"]  # Здесь можно добавить форматирование даты
            description = transaction["description"]
            masked_from = (
                get_mask_account(transaction.get("from", "")) if transaction.get("from") else "Не указано"
            )  # Маскируем номер счета
            masked_to = (
                get_mask_account(transaction.get("to", "")) if transaction.get("to") else "Не указано"
            )  # Маскируем номер счета
            print(f"{date}\t{description}\t{amount} {currency}\tОт: {masked_from}\tДо: {masked_to}")
        else:
            print(f"Транзакция пропущена: отсутствует 'operationAmount' в записи с ID {transaction.get('id')}")

    if len(transactions) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
