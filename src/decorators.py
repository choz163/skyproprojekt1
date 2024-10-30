from functools import wraps
from pathlib import Path
from typing import Any, Callable


def log(filename: str | Path | None = None) -> Callable:
    """
    Декоратор автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки.
    """

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                _log(f"{func.__name__} ok. Inputs: {args}, {kwargs}.")
            except Exception as e:
                _log(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}.")
                raise e

            return result

        def _log(msg: str) -> None:
            if filename:
                _log_file(filename, msg)
            else:
                _log_console(msg)

        def _log_console(msg: str) -> None:
            print(msg)

        def _log_file(file_path: str | Path, msg: str) -> None:
            with open(file_path, mode="a", encoding="utf-8") as f:
                f.write(msg + "\n")

        return wrapper

    return decorator
