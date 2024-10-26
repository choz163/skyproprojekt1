import os

from src.bank_transactions import find_transactions_by_description
from src.decorators import log
from src.generators import filter_by_currency
from src.masks import get_mask_account
from src.processing import filter_by_state, sort_by_date
from src.utils import load_operations



@log()
def main():
    # Приветствие пользователя
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Загрузка данных из фиксированного пути
    file_path = "C:\\Users\\Komp\\PycharmProjects\\my_project_1\\pythonProject1\\data\\operations.json"

    if os.path.isfile(file_path):
        transactions = load_operations(file_path)
    else:
        print("Файл не найден")
        return

    # Фильтрация по статусу
    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию."
            " \nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        )
        status = status.upper()
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        else:
            print('Статус операции "{}" недоступен.'.format(status))

    # Используем функцию фильтрации по статусу
    transactions = filter_by_state(transactions, status)
    print('Операции отфильтрованы по статусу "{}"'.format(status))

    # Сортировка по дате
    sort_by_date_input = input("Отсортировать операции по дате? Да/Нет\n").lower()
    if sort_by_date_input == "да":
        transactions = sort_by_date(transactions)

    # Фильтрация по рублевым транзакциям
    filter_by_rub_input = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
    if filter_by_rub_input == "да":
        transactions = filter_by_currency(transactions, "руб.")

    # Фильтрация по слову в описании
    filter_by_description_input = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"
    ).lower()
    if filter_by_description_input == "да":
        search_string = input("Введите слово для поиска: ")
        transactions = find_transactions_by_description(transactions, search_string)

    # Печать результата
    print("Распечатываю итоговый список транзакций...")
    print("Всего банковских операций в выборке: {}".format(len(transactions)))
    for transaction in transactions:
        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["name"]
        date = transaction["date"]  # Здесь можно добавить форматирование даты
        description = transaction["description"]
        masked_from = get_mask_account(transaction.get("from", ""))  # Маскируем номер счета
        masked_to = get_mask_account(transaction.get("to", ""))  # Маскируем номер счета
        print(f"{date}\t{description}\t{amount} {currency}\tОт: {masked_from}\tДо: {masked_to}")

    if len(transactions) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
