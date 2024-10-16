import json
import os


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
