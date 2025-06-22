import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_canceled(banking_transaction_data):
    """Тестирование фильтрации списка словарей по заданному статусу state"""
    filter_by_state(banking_transaction_data, 'CANCELED') == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]


def test_filter_by_state(banking_transaction_data):
    """Тестирование фильтрации списка словарей по статусу state по умолчанию"""
    filter_by_state(banking_transaction_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]


def test_filter_by_state_checking(banking_transaction_data):
    """Проверка работы функции при отсутствии словарей с указанным статусом state в списке"""
    filter_by_state(banking_transaction_data, 'CHECKING') == []


@pytest.mark.parametrize('state, expected',
                         [('CANCELED', [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                                        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                                        ]),
                          ('EXECUTED', [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                                        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                                        ])])
def test_filter_by_state_parametrize(banking_transaction_data, state, expected):
    """Тестирование фильтрации списка словарей по заданному статусу state (параметризация)"""
    filter_by_state(banking_transaction_data, state) == expected


