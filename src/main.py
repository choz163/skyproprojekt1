import codecs
import csv
import json
import os

import openpyxl

import bank_transactions


def main():
    # Приветствие пользователя
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    # Выбор файла
    choice = input()
    if choice == "1":
        file_path = input("Введите путь к JSON-файлу: ")
        if os.path.isfile(file_path):
            with codecs.open(file_path, "r", "utf-8") as f:
                transactions = json.load(f)
        else:
            print("Файл не найден")
            return
    elif choice == "2":
        file_path = input("Введите путь к CSV-файлу: ")
        if os.path.isfile(file_path):
            with open(file_path, "r") as f:
                reader = csv.reader(f)
                transactions = list(reader)
        else:
            print("Файл не найден")
            return
    elif choice == "3":
        file_path = input("Введите путь к XLSX-файлу: ")
        if os.path.isfile(file_path):
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active
            transactions = []
            for row in sheet.iter_rows(min_row=2):
                transactions.append(
                    {"date": row[0].value, "description": row[1].value, "amount": row[2].value, "state": row[3].value}
                )
        else:
            print("Файл не найден")
            return
    else:
        print("Неверный выбор")
        return

    # Фильтрация по статусу
    status = input(
        "Введите статус, по которому необходимо выполнить фильтрацию."
        " \nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
    )
    status = status.upper()
    if status not in ["EXECUTED", "CANCELED", "PENDING"]:
        print('Статус операции "{}" недоступен.'.format(status))
        return

    # Фильтрация транзакций
    transactions = [t for t in transactions if "state" in t and t["state"] == status]

    print('Операции отфильтрованы по статусу "{}"'.format(status))

    # Сортировка по дате (опционально)
    sort_by_date = input("Отсортировать операции по дате? Да/Нет\n")
    if sort_by_date.lower() == "да":
        sort_order = input("Отсортировать по возрастанию или по убыванию?\n")
        if sort_order.lower() == "по возрастанию":
            transactions.sort(key=lambda t: t["date"])
        elif sort_order.lower() == "по убыванию":
            transactions.sort(key=lambda t: t["date"], reverse=True)
        else:
            print("Неверный выбор")
            return

    # Фильтрация по рублевым транзакциям (опционально)
    filter_by_rub = input("Выводить только рублевые тразакции? Да/Нет\n")
    if filter_by_rub.lower() == "да":
        transactions = [t for t in transactions if t["operationAmount"]["currency"]["name"] == "руб."]

    # Фильтрация по слову в описании (опционально)
    filter_by_description = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    if filter_by_description.lower() == "да":
        search_string = input("Введите слово для поиска: ")
        transactions = bank_transactions.find_transactions_by_description(transactions, search_string)

    # Печать результата
    print("Распечатываю итоговый список транзакций...")
    print("Всего банковских операций в выборке: {}".format(len(transactions)))
    for transaction in transactions:
        print(
            "{}\t{}\t{}".format(
                transaction["date"], transaction["description"], transaction["operationAmount"]["amount"]
            )
        )

    if len(transactions) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
