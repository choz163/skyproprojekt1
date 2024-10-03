def log(filename=None):
    """Декоратор автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""

    def dekorator(my_function):
        def wrapper(*args, **kwargs):
            if not filename:
                print(f"{my_function.__name__} started")
                try:
                    my_function(*args, **kwargs)
                    print(f"{my_function.__name__} ok")
                    print(f"{my_function.__name__} finished")
                except Exception as e:
                    print(f"{my_function.__name__} error: {e}. Inputs: {args}, {kwargs}")
            else:
                try:
                    my_function(*args, **kwargs)
                    with open(filename, "w") as file:
                        file.write(f"{my_function.__name__} ok")
                except Exception as e:
                    with open(filename, "w") as file:
                        file.write(f"{my_function.__name__} error: {e}. Inputs: {args}, {kwargs}")

        return wrapper

    return dekorator
