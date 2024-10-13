import pytest
import unittest.mock as mock


from src.external_api import convert_currency



# transaction = {"amount": 100, "currency": "EUR"}
#
# converted_amount = convert_currency(transaction)
#
# print(converted_amount)


@pytest.fixture
def mock_requests_get():
    with mock.patch("requests.get") as mock_get:
        yield mock_get

def test_convert_currency_success():
    with mock.patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"success": True, "result": 100}
        result = convert_currency({"amount": 100, "currency": "USD"})
        assert result == 100


def test_convert_currency_success(mock_requests_get):
    mock_requests_get.return_value.json.return_value = {"success": True, "result": 100}
    result = convert_currency({"amount": 100, "currency": "USD"})
    assert result == 100

def test_convert_currency_error(mock_requests_get):
    mock_requests_get.return_value.json.return_value = {"success": False, "error": {"info": "Error message"}}
    with pytest.raises(ValueError):
        convert_currency({"amount": 100, "currency": "USD"})