from src.masks import get_mask_card_number, get_mask_account

def mask_account_card (names_card_and_check: str) -> str:
    if "Счет" in names_card_and_check:
        return get_mask_account(names_card_and_check)
    else:
        return get_mask_card_number(names_card_and_check)


print(mask_account_card("Visa Platinum 7000792289606361"))
