import json
import logging
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


logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log")
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# logger = logging.getLogger("utils")
#
# logger.info("Успешное событие")
#
# logger.error("Ошибка: не удалось выполнить операцию")
