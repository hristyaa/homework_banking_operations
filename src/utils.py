import json


def get_transactions_list(file_path):
    """Функция возвращает список словарей с данными о транзакций из json-файла"""
    try:
        with open(file_path, encoding='utf-8') as file:
            try:
                data_transactions = json.load(file)
                if data_transactions == []:
                    return []
                else:
                    return data_transactions
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []


# file_path = '../data/operations.json'
# print(get_transactions_list(file_path))
