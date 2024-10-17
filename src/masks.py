import logging

def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер банковской карты"""
    hidden_number = card_number[:21] + "******" + card_number[-4:]
    return hidden_number

def get_mask_account(account_number: str) -> str:
    """Функция маскирует цифры номера счета в банке"""
    return f"** {account_number[-4:]}"

# Настройка логирования
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log")
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Пример использования функций с логированием
if __name__ == "__main__":
    # Успешный вызов функции маскировки номера карты
    try:
        card_number = "12345678901234567890"
        masked_card_number = get_mask_card_number(card_number)
        logger.info(f"Замаскирован номер карты: {masked_card_number}")  # Логируем успешное использование функции
        print(masked_card_number)
    except Exception as e:
        logger.error(f"Ошибка при маскировке номера карты: {e}")  # Логируем ошибку

    # Успешный вызов функции маскировки номера счета
    try:
        account_number = "12345678901234567890"
        masked_account_number = get_mask_account(account_number)
        logger.info(f"Замаскирован номер счета: {masked_account_number}")  # Логируем успешное использование функции
        print(masked_account_number)
    except Exception as e:
        logger.error(f"Ошибка при маскировке номера счета: {e}")  # Логируем ошибку

    # Пример вызова функции с ошибкой (некорректный номер карты)
    try:
        masked_card_number_error = get_mask_card_number("123")  # Слишком короткий номер
        logger.info(f"Замаскирован номер карты: {masked_card_number_error}")  # Логируем успешное использование функции
    except Exception as e:
        logger.error(f"Ошибка при маскировке номера карты: {e}")  # Логируем ошибку

    # Пример вызова функции с ошибкой (некорректный номер счета)
    try:
        masked_account_number_error = get_mask_account("12")  # Слишком короткий номер
        logger.info(f"Замаскирован номер счета: {masked_account_number_error}")  # Логируем успешное использование функции
    except Exception as e:
        logger.error(f"Ошибка при маскировке номера счета: {e}")  # Логируем ошибку
