import pytest

from src.processing import filter_by_state, sort_by_date, process_bank_search, process_bank_operations


def test_filter_by_state_canceled(banking_transaction_data):
    """Тестирование фильтрации списка словарей по заданному статусу state"""
    filter_by_state(banking_transaction_data, "CANCELED") == [
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
    filter_by_state(banking_transaction_data, "CHECKING") == []


@pytest.mark.parametrize(
    "state, expected",
    [
        (
                "CANCELED",
                [
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                ],
        ),
        (
                "EXECUTED",
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                ],
        ),
    ],
)
def test_filter_by_state_parametrize(banking_transaction_data, state, expected):
    """Тестирование фильтрации списка словарей по заданному статусу state (параметризация)"""
    filter_by_state(banking_transaction_data, state) == expected


def test_sort_by_date(banking_transaction_data):
    """Тестирование сортировки списка словарей по датам в порядке убывания"""
    sort_by_date(banking_transaction_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_reverse(banking_transaction_data):
    """Тестирование сортировки списка словарей по датам в порядке возрастания"""
    sort_by_date(banking_transaction_data, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_same_date(banking_transaction_data_same_date):
    """Проверка корректности сортировки при одинаковых датах"""
    sort_by_date(banking_transaction_data_same_date) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_error_date(banking_transaction_data_error_date):
    """Тесты на работу функции с нестандартными форматами дат"""
    sort_by_date(banking_transaction_data_error_date) == [
        {"id": 41428829, "state": "EXECUTED", "date": "20.07.2025"},
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018/06/30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018/09/12T21:27:25.241689"},
        {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_process_bank_search(transactions, search):
    """ Тестирование работы функции с заданными аргументами"""
    process_bank_search(transactions, search) == [
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
        }, {
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
    ]


def test_process_bank_search_all(transactions):
    '''Проверка отработки функции при нахождении строки (независимо от регистра) в описании во всех транзакциях'''
    process_bank_search(transactions, 'перевод') == transactions


def test_process_bank_search_nothing(transactions):
    '''Проверка функции при отсутствии строки в описаниях транзакциях'''
    process_bank_search(transactions, 'Поступление') == []


def test_process_bank_search_no_description(banking_transaction_data):
    '''Отработка функции при отсутствии описания в списке транзакций'''
    process_bank_search(banking_transaction_data, 'перевод') == []


def test_process_bank_search_exception():
    ''' Отработка функции с ошибкой при передачи функции вместо списка транзакций строки'''
    result = process_bank_search('khkldfk', 'перевод')
    assert 'Возникла ошибка: "\'str\' object has no attribute \'get\'"'


def test_process_bank_operations(transactions, categories):
    '''Проверка отработки функции при правильных данных(независимо от регистра) '''
    process_bank_operations(transactions, categories) == {'Перевод организации': 2, 'Перевод со счета на счет': 2}


def test_process_bank_operations_nothing(transactions):
    '''Проверка отработки функции при отсутствии категории в транзакциях'''
    process_bank_operations(transactions, 'перевод') == {}


def test_process_bank_operations_exception(transactions):
    ''' Отработка функции с ошибкой при передачи функции вместо списка транзакций строки'''
    result = process_bank_operations('khkldfk', 'перевод')
    assert 'Возникла ошибка: "\'str\' object has no attribute \'get\'"'