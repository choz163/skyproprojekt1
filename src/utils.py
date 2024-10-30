import json
import logging

# Настройка логирования
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log")
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def load_operations(file_path: str) -> list:
    """Загружает данные о транзакциях из файла JSON."""
    logger.info(f"Загрузка операций из файла: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Загруженные данные должны быть списком.")

    logger.info(f"Загружено {len(data)} операций.")
    return data
