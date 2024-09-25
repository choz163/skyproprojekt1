from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(names_card_and_check: str) -> str:
    """Функция, которая маскирует счет или банковскую карту"""
    if "Visa Platinum" in names_card_and_check or "Maestro" in names_card_and_check:
        return get_mask_account(names_card_and_check)
    else:
        return get_mask_card_number(names_card_and_check)


def get_date(input_date: str) -> str:
    """Функция изменения формата даты"""
    return f"{input_date[8:10]}.{input_date[5:7]}.{input_date[0:4]}"
