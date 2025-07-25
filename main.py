import os
from datetime import datetime

from src.generators import filter_by_currency, filter_by_currency_code
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.readers import reader_csv_file, reader_excel_file
from src.utils import get_transactions_list
from src.widget import get_date, mask_account_card


def greetings():
    """Функция приветствия"""
    while True:
        try:
            user_input = input("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
""")
            if user_input == '1':
                file_type = 'JSON-файл'
                transactions = get_transactions_list(
                    os.path.abspath(os.path.join(os.path.dirname(__file__), "data", "operations.json")))
                break
            elif user_input == '2':
                file_type = 'CSV-файл'
                transactions = reader_csv_file(
                    os.path.abspath(os.path.join(os.path.dirname(__file__), "data", "transactions.csv")))
                break
            elif user_input == '3':
                file_type = 'XLSX-файл'
                transactions = reader_excel_file(
                    os.path.abspath(os.path.join(os.path.dirname(__file__), "data", "transactions_excel.xlsx")))
                break
            else:
                print('Пункт введен неккоректно')
        except Exception:
            print('Произошла ошибка')
    print(f'Для обработки выбран {file_type}')
    return transactions


def get_filtered_transaction(transactions):
    '''Функция выбора статуса для фильтрации'''
    while True:
        try:
            user_input_status = input("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
""")
            if user_input_status.upper() in ['EXECUTED', 'CANCELED', 'PENDING']:
                filtered_transactions = filter_by_state(transactions, user_input_status.upper())
                return filtered_transactions
                break
            else:
                print(f'Статус операции {user_input_status} недоступен')
        except Exception as ex:
            print(f'Произошла ошибка {ex}')


if __name__ == '__main__':
    transactions = greetings()
    filtered_transactions = get_filtered_transaction(transactions)

    try:
        while True:
            user_input_sort_of_date = input("""Отсортировать операции по дате? Да/Нет
""").lower()
            if user_input_sort_of_date == 'да':
                while True:
                    user_input_sort_of_date_reverse = input("""Отсортировать по возрастанию или по убыванию?
""").lower()
                    if user_input_sort_of_date_reverse == 'по возрастанию':
                        filtered_transactions = sort_by_date(filtered_transactions, reverse=False)
                        break
                    elif user_input_sort_of_date_reverse == 'по убыванию':

                        filtered_transactions = sort_by_date(filtered_transactions, reverse=True)
                        break
                    else:
                        print('Неверный ввод')
                break

            elif user_input_sort_of_date == 'нет':
                break
            else:
                print('Неверный ввод')

        while True:
            user_input_rub = input("""Выводить только рублевые транзакции? Да/Нет
""").lower()
            if user_input_rub == 'да':
                for transaction in filtered_transactions:
                    if transaction.get('currency_name') is not None:
                        flag = 1
                        break
                    elif transaction.get('operationAmount') is not None:
                        flag = 0
                if flag == 1:
                    filtered_transactions = list(filter_by_currency_code(filtered_transactions, 'RUB'))

                if flag == 0:
                    filtered_transactions = list(filter_by_currency(filtered_transactions, 'руб.'))
                break
            elif user_input_rub == 'нет':
                break
            else:
                print('Неверный ввод')
        while True:
            user_input_description = input("""Отфильтровать список транзакций по определенному слову в описании? Да/Нет
""").lower()
            if user_input_description == 'да':
                search = input("""Введите слово в описании для фильтрации
""")
                filtered_transactions = process_bank_search(filtered_transactions, search)
                break
            elif user_input_description == 'нет':
                break
            else:
                print('Неверный ввод')
        print('Распечатываю итоговый список транзакций...')

        if len(filtered_transactions) == 0:
            print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')

        print(f'Всего банковских операций в выборке: {len(filtered_transactions)}\n')

        for filtered_transaction in filtered_transactions:
            if filtered_transaction['description'] != 'Открытие вклада':
                try:
                    print(f"""{get_date(filtered_transaction["date"])} {filtered_transaction['description']}
{mask_account_card(filtered_transaction['from'])} - > {mask_account_card(filtered_transaction['to'])}""")
                except ValueError:
                    date = datetime.strptime(filtered_transaction["date"], "%Y-%m-%dT%H:%M:%SZ")
                    print(f"""{date.strftime("%d.%m.%Y")} {filtered_transaction['description']}
{mask_account_card(filtered_transaction['from'])} - > {mask_account_card(filtered_transaction['to'])}""")
                except Exception as ex:
                    print(f'Произошла ошибка {ex}')
            else:
                try:
                    print(f"""{get_date(filtered_transaction["date"])} {filtered_transaction['description']}
{mask_account_card(filtered_transaction['to'])}""")
                except ValueError:
                    date = datetime.strptime(filtered_transaction["date"], "%Y-%m-%dT%H:%M:%SZ")
                    print(f"""{date.strftime("%d.%m.%Y")} {filtered_transaction['description']}
{mask_account_card(filtered_transaction['to'])}""")
                except Exception as ex:
                    print(f'Произошла ошибка {ex}')

            if filtered_transaction.get('operationAmount') is not None:
                print(
                    f"Сумма: {filtered_transaction['operationAmount']['amount']} "
                    f"{filtered_transaction['operationAmount']['currency']['name']}\n")
            else:
                print(f'Сумма: {filtered_transaction['amount']} {filtered_transaction['currency_code']}\n')

    except Exception as ex:
        print(f'Произошла ошибка {ex}')
