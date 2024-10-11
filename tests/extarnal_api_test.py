import unittest.mock as mock

import pytest
import requests

from src.external_api import convert_currency

# amount = 100
# from_currency = "USD"
# to_currency = "EUR"
#
# converted_amount = convert_currency(amount, from_currency, to_currency)
#
# print(converted_amount)


@pytest.fixture
def mock_requests_get():
    with mock.patch("requests.get") as mock_get:
        yield mock_get


def test_valid_conversion(mock_requests_get):
    mock_requests_get.return_value = mock.Mock(json=lambda: {"success": True, "result": 110.0})
    result = convert_currency(100, "EUR", "USD")
    assert result == 110.0


def test_invalid_conversion(mock_requests_get):
    mock_requests_get.return_value = mock.Mock(json=lambda: {"success": False, "error": {"info": "Invalid currency"}})
    with pytest.raises(ValueError):
        convert_currency(100, "EUR", "INVALID")
