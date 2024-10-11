import json
import os
import unittest.mock as mock

import pytest

from src.external_api import convert_currency
from src.utils import get_transaction_rub, load_operations


@pytest.fixture
def mock_convert_currency():
    with mock.patch("src.external_api.convert_currency") as mock_convert:
        yield mock_convert


def test_valid_rub_transaction(mock_convert_currency):
    transaction = {"amount": 100, "currency": "RUB"}
    result = get_transaction_rub(transaction)
    assert result == 100.0
    mock_convert_currency.assert_not_called()


def test_invalid_currency_transaction():
    transaction = {"amount": 100, "currency": "INVALID"}
    with pytest.raises(ValueError):
        get_transaction_rub(transaction)


def test_load_valid_json():
    json_data = [{"amount": 100, "currency": "RUB"}]
    json_file = "test.json"
    with open(json_file, "w") as f:
        json.dump(json_data, f)

    result = load_operations(json_file)
    assert result == json_data

    os.remove(json_file)


def test_valid_rub_transaction(mock_convert_currency):
    transaction = {"amount": 100, "currency": "RUB"}
    result = get_transaction_rub(transaction)
    assert result == 100.0
    mock_convert_currency.assert_not_called()


def test_invalid_currency_transaction():
    transaction = {"amount": 100, "currency": "INVALID"}
    with pytest.raises(ValueError):
        get_transaction_rub(transaction)
