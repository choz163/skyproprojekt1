import pytest
import unittest.mock as mock
from pathlib import Path
from src.decorators import log  # Замените на правильный путь к вашему модулю

@pytest.fixture
def mock_print():
    with mock.patch("builtins.print") as mock_print:
        yield mock_print

def test_log_console(mock_print):
    @log()
    def test_function():
        return "test"

    test_function()
    mock_print.assert_called_once_with("test_function ok. Inputs: (), {}.")

def test_log_file():
    file_path = Path("test.log")
    file_path.touch()

    @log(filename=file_path)
    def test_function():
        return "test"

    test_function()

    with open(file_path, "r") as f:
        log_message = f.read()
        assert log_message == "test_function ok. Inputs: (), {}.\n"

    file_path.unlink()  # Удаляем файл после теста

def test_log_error(mock_print):
    @log()
    def test_function():
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        test_function()

    mock_print.assert_called_once_with("test_function error: Test error. Inputs: (), {}.")

def test_log_file_error():
    file_path = Path("test.log")
    file_path.touch()

    @log(filename=file_path)
    def test_function():
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        test_function()

    with open(file_path, "r") as f:
        log_message = f.read()
        assert log_message == "test_function error: Test error. Inputs: (), {}.\n"

    file_path.unlink()  # Удаляем файл после теста

def test_log_decorator_preserves_function_signature():
    def test_function(a: int, b: str) -> float:
        return a + len(b)

    decorated_function = log()(test_function)
    assert decorated_function.__name__ == "test_function"
    assert decorated_function.__doc__ == test_function.__doc__
    assert decorated_function.__annotations__ == test_function.__annotations__


#
#
# @log()
# def my_function(x, y):
#     return x / y
#
#
# def test_log_print(capsys):
#     my_function(10, 5)
#     captured = capsys.readouterr()
#     expected_output = "my_function started\n" "my_function ok\n" "my_function finished\n"
#     assert captured.out == expected_output
#
#
# def test_log_print_try(capsys):
#     my_function(10, 0)
#     captured = capsys.readouterr()
#     expected_output = "my_function started\n" "my_function error: division by zero. Inputs: (10, 0), {}\n"
#     assert captured.out == expected_output
#
#
# def test_log_print_fail(tmp_path):
#     log_file = tmp_path / "test_output.txt"
#
#     @log(log_file)
#     def my_function(x, y):
#         return x / y
#
#     my_function(10, 5)
#     with open(log_file, "r") as f:
#         content = f.read()
#     assert content == "my_function ok"
#
#
# def test_log_print_fail_try(tmp_path):
#     log_file = tmp_path / "test_output.txt"
#
#     @log(log_file)
#     def my_function(x, y):
#         return x / y
#
#     my_function(10, 0)
#     with open(log_file, "r") as f:
#         content = f.read()
#     assert content == "my_function error: division by zero. Inputs: (10, 0), {}"
