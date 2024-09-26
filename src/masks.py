def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер банковской карты"""
    hidden_number = card_number[:21] + "******" + card_number[-4:]
    return hidden_number


def get_mask_account(account_number: str) -> str:
    """Функция маскирует цифры номера счета в банке"""
    return f"** {account_number[-4:]}"
