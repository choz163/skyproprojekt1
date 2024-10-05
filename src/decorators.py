from functools import wraps


def log(filename=None):
    """Декоратор автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""
    def dekorator(my_func):
        @wraps(my_func)
        def wrapper(*args, **kwargs):
            if not filename:
                print(f'{my_func.__name__} started')
                try:
                    my_func(*args, **kwargs)
                    print(f'{my_func.__name__} ok')
                    print(f'{my_func.__name__} finished')
                except Exception as e:
                    print(f'{my_func.__name__} error: {e}. Inputs: {args}, {kwargs}')
            else:
                try:
                    my_func(*args, **kwargs)
                    with open(filename, 'w') as file:
                        file.write(f'{my_func.__name__} ok')
                except Exception as e:
                    with open(filename, 'w') as file:
                        file.write(f'{my_func.__name__} error: {e}. Inputs: {args}, {kwargs}')
            # return result
        return wrapper
    return dekorator


@log()
def my_function(x, y):
    return x / y


my_function(10, 5)

