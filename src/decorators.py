from functools import wraps


def log(filename=None):
    """ Декоратор, который логирует начало и конец выполнения функции, а также ее результаты или ошибки."""
    def decorate(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename == None:
                    print(f'{func.__name__} ok, result: {result}')
                else:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f'{func.__name__} ok, result: {result}\n')
            except Exception as e:
                if filename == None:
                    print(f'{func.__name__} error: {e}, Inputs: {args}, {kwargs}')
                else:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f'{func.__name__} error: {e}, Inputs: {args}, {kwargs}\n')
        return wrapper
    return decorate


@log(filename="mylog.txt")
def my_function(x, y):
    return x / y

my_function(1, 2)
