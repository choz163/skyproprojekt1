import pytest

from src.masks import get_mask_account, get_mask_card_number

print(get_mask_card_number("Visa Platinum 7000792289606361"))
print(get_mask_account("73654108430135874305"))


@pytest.fixture()
def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "700079******6361"


@pytest.mark.parametrize(
    "account_number, hid_number",
    [("73654108430135874305", "** 4305"), ("45687951452364781242", "** 1242"), ("2548779665412345578", "** 5578")],
)
def test_get_mask_account(account_number, hid_number):
    assert get_mask_account(account_number) == hid_number
