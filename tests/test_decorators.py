import os
import pytest

from src.decorators import log


def test_log(capsys):
    """Проверка на успешное выполнение функции"""

    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok, result: 3\n"


def test_log_exception(capsys):
    """Проверка на выполнение функции с ошибкой"""

    @log()
    def my_function(x, y):
        return x / y


    my_function(1, 0)

    captured = capsys.readouterr()
    assert captured.out == "my_function error: division by zero, Inputs: (1, 0), {}\n"


def test_log_in_file():
    """Проверка на успешное выполнение функции и с ошибкой,проверка записи лога в файл"""
    if os.path.exists("mylog.txt"):
        os.remove("mylog.txt")

    @log(filename="mylog.txt")
    def my_function(x, y):
        return x / y

    my_function(1, 0)
    with open("mylog.txt", "r", encoding="utf-8") as file:
        text = file.read()

    assert text == "my_function error: division by zero, Inputs: (1, 0), {}\n"

    if os.path.exists("mylog.txt"):
        os.remove("mylog.txt")

    my_function(1, 2)
    with open("mylog.txt", "r", encoding="utf-8") as file:
        text = file.read()

    assert text == "my_function ok, result: 0.5\n"


