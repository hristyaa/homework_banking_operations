# from utils import get_transactions_list
import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')


def get_amount_of_transaction(transaction):
    """Функция обрабатывает транзакцию и возвращает сумму транзакции в рублях,
    при необхожимости конвертируя ее из USD или EUR"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return transaction["operationAmount"]["amount"]
    else:
        url = "https://api.apilayer.com/exchangerates_data/convert"
        payload = {"amount": transaction["operationAmount"]["amount"],
                   "from": transaction["operationAmount"]["currency"]["code"], "to": "RUB"}
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers, params=payload)
        if response.status_code != 200:
            raise ValueError("Failed to get currency rate")
        return response.json()['result']


transaction = {
    "id": 114832369,
    "state": "EXECUTED",
    "date": "2019-12-07T06:17:14.634890",
    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "Visa Classic 2842878893689012",
    "to": "Счет 35158586384610753655",
}
print(get_amount_of_transaction(transaction))

# file_path = '../data/operations.json'
# data_transactions = get_transactions_list(file_path)
# get_amount_of_transaction(data_transactions)
