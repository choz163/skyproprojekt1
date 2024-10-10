import requests
import json
from pathlib import Path


def load_operations(path: Path) -> list[dict]:
    """ Загружает данные финансовых транзакций из файла JSON. """

    if not path.exists():
        return []

    with open(path, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []

    if not isinstance(data, list):
        return []

    return data

