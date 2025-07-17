import pandas as pd


def reader_csv_file(file_csv_path):
    """Функция считывает финансовые операции из CSV и выдает список словарей с транзакциями."""
    try:
        transaction_csv = pd.read_csv(file_csv_path)
        return transaction_csv.to_json(orient="records", indent=4)

    except FileNotFoundError:
        return "Файл не найден."
    except pd.errors.EmptyDataError:
        return "Файл пустой."
    except Exception as ex:
        return f"Произошла ошибка: {ex}."


def reader_excel_file(file_excel_path):
    """Функция считывает финансовые операции из Excel и выдает список словарей с транзакциями."""
    try:
        transaction_excel = pd.read_excel(file_excel_path)
        return transaction_excel.to_json(orient="records", indent=4)

    except FileNotFoundError:
        return "Файл не найден."
    except pd.errors.EmptyDataError:
        return "Файл пустой."
    except ValueError as ve:
        if "Excel file format cannot be determined" in str(ve):
            return "Файл пустой."
        return f"Произошла ошибка: {ve}."
    except Exception as ex:
        return f"Произошла ошибка: {ex}."


file_csv_path = "../data/transactions.csv"
print(reader_csv_file(file_csv_path))

# file_excel_path = '../data/transactions_excel.xlsx'
# print(reader_excel_file(file_excel_path))
