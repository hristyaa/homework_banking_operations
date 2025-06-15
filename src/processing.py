def filter_by_state(banking_transaction_data: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция фильтрует список банковских операций по статусу"""
    new_list_data = []
    for operations_by_status in banking_transaction_data:
        if operations_by_status.get('state') == state:
            new_list_data.append(operations_by_status)
    return new_list_data

print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], 'CANCELED'))