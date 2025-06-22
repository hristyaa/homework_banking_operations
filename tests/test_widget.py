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

