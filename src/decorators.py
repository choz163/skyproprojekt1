from functools import wraps


def log(filename=None):
    """Декоратор автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""
    def dekorator(my_func):
        @wraps(my_func)
        def wrapper(*args, **kwargs):
            result = None
            if not filename:
                print(f'{my_func.__name__} started')
                try:
                    result = my_func(*args, **kwargs)
                    print(f'{my_func.__name__} ok')
                    print(f'{my_func.__name__} finished')
                except Exception as e:
                    print(f'{my_func.__name__} error: {e}. Inputs: {args}, {kwargs}')
                    print(f'{my_func.__name__} error: {e}')
                    raise
            else:
                try:
                    result = my_func(*args, **kwargs)
                    with open(filename, 'w') as file:
                        file.write(f'{my_func.__name__} ok')
                except Exception as e:
                    with open(filename, 'w') as file:
                        file.write(f'{my_func.__name__} error: {e}. Inputs: {args}, {kwargs}')
                        raise
            return result
        return wrapper
    return dekorator
