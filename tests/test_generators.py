import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.mark.parametrize(
    "currency, expected",
    [
        ("USD",
         [
             {
                 "id": 939719570,
                 "state": "EXECUTED",
                 "date": "2018-06-30T02:08:58.425572",
                 "operationAmount": {
                     "amount": "9824.07",
                     "currency": {
                         "name": "USD",
                         "code": "USD"
                     }
                 },
                 "description": "Перевод организации",
                 "from": "Счет 75106830613657916952",
                 "to": "Счет 11776614605963066702"
             },
             {
                 "id": 142264268,
                 "state": "EXECUTED",
                 "date": "2019-04-04T23:20:05.206878",
                 "operationAmount": {
                     "amount": "79114.93",
                     "currency": {
                         "name": "USD",
                         "code": "USD"
                     }
                 },
                 "description": "Перевод со счета на счет",
                 "from": "Счет 19708645243227258542",
                 "to": "Счет 75651667383060284188"
             },
             {
                 "id": 895315941,
                 "state": "EXECUTED",
                 "date": "2018-08-19T04:27:37.904916",
                 "operationAmount": {
                     "amount": "56883.54",
                     "currency": {
                         "name": "USD",
                         "code": "USD"
                     }
                 },
                 "description": "Перевод с карты на карту",
                 "from": "Visa Classic 6831982476737658",
                 "to": "Visa Platinum 8990922113665229"
             }
         ]
         ),
        ("руб.",
         [
             {
                 "id": 873106923,
                 "state": "EXECUTED",
                 "date": "2019-03-23T01:09:46.296404",
                 "operationAmount": {
                     "amount": "43318.34",
                     "currency": {
                         "name": "руб.",
                         "code": "RUB"
                     }
                 },
                 "description": "Перевод со счета на счет",
                 "from": "Счет 44812258784861134719",
                 "to": "Счет 74489636417521191160"
             },
             {
                 "id": 594226727,
                 "state": "CANCELED",
                 "date": "2018-09-12T21:27:25.241689",
                 "operationAmount": {
                     "amount": "67314.70",
                     "currency": {
                         "name": "руб.",
                         "code": "RUB"
                     }
                 },
                 "description": "Перевод организации",
                 "from": "Visa Platinum 1246377376343588",
                 "to": "Счет 14211924144426031657"
             }
         ])
    ]
)
def test_filter_by_currency(transactions, currency, expected):
    """Проверка, что функция корректно фильтрует транзакции по заданной валюте"""
    result = list(filter_by_currency(transactions, currency))
    assert result == expected


@pytest.mark.parametrize("currency, expected", [('yuan', []), ('EUR', [])])
def test_filter_by_currency_absent(transactions, currency, expected):
    """Проверка фильтрации отсутствующих валют"""
    result = list(filter_by_currency(transactions, currency))
    assert result == expected


@pytest.mark.parametrize("transactions, currency, expected", [([], 'EUR', [])])
def test_filter_by_currency_absent_transactions(transactions, currency, expected):
    """Проверка фильтрации пустого списка транзакций"""
    result = list(filter_by_currency(transactions, currency))
    assert result == expected


def test_transaction_descriptions(transactions):
    """Проверка, что функция корректно отображает операции """
    gen = transaction_descriptions(transactions)
    assert next(gen) == 'Перевод организации'
    assert next(gen) == 'Перевод со счета на счет'
    assert next(gen) == 'Перевод со счета на счет'
    assert next(gen) == 'Перевод с карты на карту'
    assert next(gen) == 'Перевод организации'


def test_transaction_descriptions_absent_transactions(transactions):
    """Проверка, что функция корректно обрабатывает пустой список транзакций """
    gen = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(gen)


@pytest.mark.parametrize("a, b, expected", [(1, 5, ['0000 0000 0000 0001',
                                                    '0000 0000 0000 0002',
                                                    '0000 0000 0000 0003',
                                                    '0000 0000 0000 0004',
                                                    '0000 0000 0000 0005']),
                                            (74123, 74125, ['0000 0000 0007 4123',
                                                            '0000 0000 0007 4124',
                                                            '0000 0000 0007 4125'])
                                            ])
def test_card_number_generator(a, b, expected):
    """Проверка, что генератор выдает правильные номера карт в заданном диапазоне"""
    result = list(card_number_generator(a, b))
    assert result == expected

def test_card_number_generator_empty_range():
    """Проверка, что функция корректно обрабатывает пустой диапазон """
    gen = card_number_generator(71,71)
    assert next(gen) == "0000 0000 0000 0071"
    with pytest.raises(StopIteration):
        next(gen)


def test_card_number_generator_extreme_values():
    """Проверка, что функция корректно обрабатывает крайние значения """
    assert next(card_number_generator(1,1)) == "0000 0000 0000 0001"
    assert next(card_number_generator(9999999999999999, 9999999999999999)) == "9999 9999 9999 9999"


def test_card_number_generator_incorrect_range():
    """Проверка, что функция корректно обрабатывает неверный диапазон """
    gen = card_number_generator(0,0)
    with pytest.raises(ValueError):
        next(gen)
    gen = card_number_generator(5, 1)
    with pytest.raises(ValueError):
        next(gen)
    gen = card_number_generator(1, 10000000000000000)
    with pytest.raises(ValueError):
        next(gen)
