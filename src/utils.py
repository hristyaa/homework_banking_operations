import json
import logging
import os

utils_logger = logging.getLogger("app.utils")

log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "logs"))
os.makedirs(log_dir, exist_ok=True)

file_handler = logging.FileHandler(filename=os.path.join(log_dir, "utils.log"), mode="w", encoding="utf-8")

file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)


def get_transactions_list(file_path):
    """Функция возвращает список словарей с данными о транзакций из json-файла"""
    utils_logger.info("Попытка открытия json-файла")
    try:
        with open(file_path, encoding="utf-8") as file:
            utils_logger.info("Файл успешно открылся")
            try:
                utils_logger.info("Проверка содержимого json-файла")
                data_transactions = json.load(file)
                if data_transactions == []:
                    utils_logger.info("Файл содержит пустой список")
                    return []
                else:
                    utils_logger.info("Файл содержит данные с транзакциями")
                    return data_transactions
            except json.JSONDecodeError:
                utils_logger.error("Файл пустой")
                return []
    except FileNotFoundError:
        utils_logger.error("Файл не найден")
        return []


# file_path = '../data/operations.json'
# print(get_transactions_list(file_path))
