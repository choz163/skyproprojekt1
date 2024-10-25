import csv

import pandas as pd


def read_csv(file_path: str) -> list[dict]:
    """Считывает финансовые операции из CSV-файла."""
    with open(file_path, "r") as f:
        reader = csv.DictReader(f, delimiter=";")  # Указываем разделитель
        return list(reader)


def read_excel(file_path: str) -> list[dict]:
    """Считывает финансовые операции из Excel-файла."""
    df = pd.read_excel(file_path)
    return df.to_dict("records")
