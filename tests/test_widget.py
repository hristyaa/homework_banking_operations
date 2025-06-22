import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('user_input, expected', [('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                                                ('Счет 73654108430135870001', 'Счет **0001'),
                                                ('Maestro 7000792289604567', 'Maestro 7000 79** **** 4567')])
def test_mask_account_card(user_input, expected):
    """проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных данных"""
    assert mask_account_card(user_input) == expected

def test_mask_account_card_invalid_account_card():
    """Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты"""
    with pytest.raises(ValueError):
        mask_account_card('')

def test_mask_account_card_invalid_account_card():
    """Проверка, что функция корректно обрабатывает входные строки, где некорректный номер карты"""
    with pytest.raises(ValueError):
        mask_account_card('Visa Platinum 7361254108430135870001')


@pytest.mark.parametrize('date, expected',
                         [('2024-03-11T02:26:18.671407', '11.03.2024'),
                          ('2025-07-20T02:22:13.141427', '20.07.2025'),
                          ('2021-07-17T02:24:17.175407', '17.07.2021')])
def test_get_date(date, expected):
    """Проверка, что функция корректно обрабатывает различных входные данные"""
    get_date(date) == expected
def test_get_date_invalid_date():
    """Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата"""
    with pytest.raises(ValueError):
        get_date('')

def test_get_date_invalid_date_1():
    """Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата"""
    with pytest.raises(ValueError):
        get_date('2078945115')
