import csv
from typing import Any, Dict, List

import openpyxl


def read_csv(file_path: str) -> List[Dict[str, Any]]:
    """Читает данные из CSV-файла и возвращает список транзакций."""
    transactions = []
    with open(file_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            # Проверка на наличие id
            if row["id"] == "":
                continue  # Пропускаем запись, если id пустой

            transactions.append(
                {
                    "id": int(row["id"]),
                    "state": row["state"],
                    "date": row["date"],
                    "operationAmount": {
                        "amount": row["amount"],
                        "currency": {"name": row["currency_name"], "code": row["currency_code"]},
                    },
                    "from": row["from"],
                    "to": row["to"],
                    "description": row["description"],
                }
            )
    return transactions


def read_excel(file_path: str) -> List[Dict[str, Any]]:
    """Читает данные из XLSX-файла и возвращает список транзакций."""
    transactions = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        if row[0] is None:  # Проверка на пустое значение id
            continue  # Пропускаем запись, если id пустой

        transactions.append(
            {
                "id": int(row[0]),
                "state": row[1],
                "date": row[2],
                "operationAmount": {"amount": row[3], "currency": {"name": row[4], "code": row[5]}},
                "from": row[6],
                "to": row[7],
                "description": row[8],
            }
        )
    return transactions
