import unittest.mock as mock

import pytest

from src.external_api import convert_currency

# transaction = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}
#
# converted_amount = convert_currency(transaction)
# print(converted_amount)

@pytest.fixture
def mock_requests_get():
    with mock.patch("requests.get") as mock_get:
        yield mock_get


def test_convert_currency_success(mock_requests_get):
    mock_requests_get.return_value.json.return_value = {"success": True, "result": 100}
    transaction = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}
    result = convert_currency(transaction)
    assert result == 100


def test_convert_currency_error(mock_requests_get):
    mock_requests_get.return_value.json.return_value = {"success": False, "error": {"info": "Error message"}}
    transaction = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}
    with pytest.raises(ValueError):
        convert_currency(transaction)
