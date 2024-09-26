import pytest

from src.widget import get_date, mask_account_card

print(mask_account_card("Visa Platinum 7000792289606361"))
print(get_date("2024-03-11T02:26:18.671407"))


@pytest.mark.parametrize(
    "inp_check_number, hid_check_number",
    [
        ("Visa Platinum 70007922879606361", "** 6361"),
        ("Maestro 70005768759549128", "** 9128"),
        ("Visa Platinum 70008848576400987", "** 0987"),
    ],
)
def test_mask_account_card(inp_check_number, hid_check_number):
    assert mask_account_card(inp_check_number) == hid_check_number


@pytest.mark.parametrize(
    "inp_date, new_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-06-24T04:30:21.487517", "24.06.2024"),
        ("2024-01-22T06:12:14.987461", "22.01.2024"),
        ("2024-06-14", "14.06.2024"),
    ],
)
def test_get_date(inp_date, new_date):
    assert get_date(inp_date) == new_date
