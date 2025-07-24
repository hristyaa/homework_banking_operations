import re
from collections import Counter

def filter_by_state(banking_transaction_data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрует список банковских операций по статусу."""
    new_list_data = []
    for operations_by_status in banking_transaction_data:
        if operations_by_status.get("state") == state:
            new_list_data.append(operations_by_status)
    return new_list_data


def sort_by_date(banking_transaction_data: list[dict], reverse: bool = True) -> list[dict]:
    """Функция сортирует список банковских операций по дате (по умолчанию - по убыванию)."""
    sorted_banking_transaction_data = sorted(
        banking_transaction_data, key=lambda operation: str(operation.get("date")), reverse=reverse
    )
    return sorted_banking_transaction_data


def process_bank_search(banking_transaction_data:list[dict], search:str)->list[dict]:
    """ Функция возвращает список словарей транзакций, в которых в описании есть данная строка"""
    try:
        pattern = re.compile(search, re.IGNORECASE)
        new_data = []
        for transaction in banking_transaction_data:
            if pattern.search(transaction.get('description')) is not None:
                new_data.append(transaction)
        return new_data
    except Exception as ex:
        return f'Возкникла ошибка:"{ex}"'


def process_bank_operations(banking_transaction_data:list[dict], categories:list)->dict:
    """ Функция возвращает словарь, в котором ключи - это названия категорий операций, а значения - количество операций в каждой категории"""
    try:
        categories_lower = [category.lower() for category in categories]
        descriptions = [transaction.get('description') for transaction in banking_transaction_data if transaction.get('description').lower() in categories_lower]
        counter = Counter()
        for description in descriptions:
            counter[description] += 1
        return dict(counter)
    except Exception as ex:
        return f"Произошла ошибка {ex}"


# print(
#     process_bank_operations(
#         [
#             {"id": 41428829, "description": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "description": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "description": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "description": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ], ['executed', 'call', 'called', 'caNcEleD']
#     )
# )

# print(
#     filter_by_state(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ]
#     )
# )
#
# print(
#     sort_by_date(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ]
#     )
# )
