import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number_1():
    """Тестирование правильности маскирования номера карты"""
    assert get_mask_card_number(2200456778991122) == '2200 45** **** 1122'


@pytest.mark.parametrize('card_number, expected', [(7000792289606361, '7000 79** **** 6361'),
                                                (7000792289604785, '7000 79** **** 4785'),
                                                ('7000792289606361', '7000 79** **** 6361')])
def test_get_mask_card_number_2(card_number, expected):
    """Проверка работы функции на различных форматах входных данных номеров карт"""
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_invalid_card_number_0():
    """Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты"""
    with pytest.raises(ValueError):
        get_mask_card_number('')


def test_get_mask_card_number_invalid_card_number_lenght():
    """Проверка, что функция корректно обрабатывает входные строки, где длина номера карты неправильная"""
    with pytest.raises(ValueError):
        get_mask_card_number(7000792289604785123)


def test_get_mask_account():
    """Тестирование правильности маскирования номера счета"""
    assert get_mask_account(73654108430135874305) == '**4305'


@pytest.mark.parametrize('account_number, expected', [(73654108430135877894, '**7894'),
                                                (73654108430135870001, '**0001'),
                                                ('73654108430135877777', '**7777')])
def test_get_mask_account_1(account_number, expected):
    """Проверка работы функции на различных форматах входных данных номеров счета"""
    assert get_mask_account(account_number) == expected


def test_get_mask_card_account_invalid_account_number_0():
    """Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты"""
    with pytest.raises(ValueError):
        get_mask_account('')


def test_get_mask_card_account_invalid_account_number_lenght():
    """Проверка, что функция корректно обрабатывает входные строки, где длина номера карты неправильная"""
    with pytest.raises(ValueError):
        get_mask_account(7000792289604785123)
