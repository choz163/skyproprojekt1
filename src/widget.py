from src.masks import get_mask_card_number, get_mask_account


def mask_account_card (names_card_and_check: str) -> str:
    """Функция которая маскирует счет или банковскую карту"""
    if "Счет" in names_card_and_check:
        return get_mask_account(names_card_and_check)
    else:
        return get_mask_card_number(names_card_and_check)


print(mask_account_card("Visa Platinum 7000792289606361"))


def get_date(input_date: str) -> str:
    """Функция изменение формата даты"""
    return f"{input_date[8:10]}.{input_date[5:7]}.{input_date[0:4]}"

print(get_date("2024-03-11T02:26:18.671407"))