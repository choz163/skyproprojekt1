def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер банковской карты"""
    hidden_number = card_number[:21] + "** ****" + card_number[-4:]
    return hidden_number
    # Скрываем символы номера карты
    # hidden_chars = [20, 21, 22, 23, 24, 25]
    # hidden_numbers = ""
    # for number, char in enumerate(card_number):
    #     if number in hidden_chars:
    #         hidden_numbers += "*"
    #     else:
    #         hidden_numbers += char
    # # Разбитие номера карты на блоки
    # breaking = [
    #     hidden_numbers[0:12],
    #     hidden_numbers[12:16],
    #     hidden_numbers[16:20],
    #     hidden_numbers[20:24],
    #     hidden_numbers[24:28],
    # ]
    #
    # return " ".join(breaking)
    # return hidden_numbers

# print(get_mask_card_number("Visa Platinum 7000792289606361"))


def get_mask_account(account_number: str) -> str:
    """Функция маскирует цифры номера счета в банке"""
    return f"** {account_number[-4:]}"


# print(get_mask_account("73654108430135874305"))
