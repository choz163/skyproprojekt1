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


# from functools import wraps
#
#
# def log(filename=None):
#     """Декоратор автоматически логирует начало и конец выполнения функции,
#     а также ее результаты или возникшие ошибки."""
#     def decorator(my_func):
#         @wraps(my_func)
#         def wrapper(*args, **kwargs):
#             result = None
#             if not filename:
#                 print(f'{my_func.__name__} started')
#                 try:
#                     result = my_func(*args, **kwargs)
#                     print(f'{my_func.__name__} ok')
#                     print(f'{my_func.__name__} finished')
#                 except Exception as e:
#                     print(f'{my_func.__name__} error: {e}. Inputs: {args}, {kwargs}')
#                     print(f'{my_func.__name__} error: {e}')
#                     raise
#             else:
#                 try:
#                     result = my_func(*args, **kwargs)
#                     with open(filename, 'w') as file:
#                         file.write(f'{my_func.__name__} ok')
#                 except Exception as e:
#                     with open(filename, 'w') as file:
#                         file.write(f'{my_func.__name__} error: {e}. Inputs: {args}, {kwargs}')
#                         raise
#             return result
#         return wrapper
#     return decorator
