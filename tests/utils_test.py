import json  # Добавьте этот импорт
import unittest.mock as mock
import pytest
from src.utils import load_operations


@pytest.fixture
def mock_os_path_exists():
    with mock.patch("os.path.exists") as mock_exists:
        yield mock_exists


@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as mock_open:
        yield mock_open


def test_load_operations_success(mock_os_path_exists, mock_open):
    mock_os_path_exists.return_value = True
    mock_open.return_value.__enter__.return_value.read.return_value = '[{"id": 1, "state": "EXECUTED"}]'

    result = load_operations("path/to/file.json")
    assert result == [{"id": 1, "state": "EXECUTED"}]


def test_load_operations_file_not_found(mock_os_path_exists):
    mock_os_path_exists.return_value = False
    with pytest.raises(FileNotFoundError):
        load_operations("path/to/file.json")


def test_load_operations_invalid_json(mock_os_path_exists, mock_open):
    mock_os_path_exists.return_value = True
    mock_open.return_value.__enter__.return_value.read.return_value = "invalid json"

    with pytest.raises(json.JSONDecodeError):
        load_operations("path/to/file.json")


def test_load_operations_not_a_list(mock_os_path_exists, mock_open):
    mock_os_path_exists.return_value = True
    mock_open.return_value.__enter__.return_value.read.return_value = "{}"

    with pytest.raises(ValueError):
        load_operations("path/to/file.json")
