def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер банковской карты"""
    # Скрываем символы номера карты
    hidden_chars = [6, 7, 8, 9, 10, 11]
    hidden_numbers = ""
    for number, char in enumerate(card_number):
        if number in hidden_chars:
            hidden_numbers += "*"
        else:
            hidden_numbers += char
    # Разбитие номера карты на блоки
    breaking = [
        hidden_numbers[0:4],
        hidden_numbers[4:8],
        hidden_numbers[8:12],
        hidden_numbers[12:16],
    ]

    return " ".join(breaking)


print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_number: str) -> str:
    """Функция маскирует цифры номера счета в банке"""
    return f"** {account_number[-4:]}"


print(get_mask_account("73654108430135874305"))
