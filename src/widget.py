from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_input: str) -> str:
    """Функция, которая возвращает замаскированный номер карты или счета"""
    user_input_split = user_input.split(" ")  # разделение введенных данных по пробелам
    type_user_card = " ".join(user_input_split[0:-1]) # занесение в переменную тип карты/счет
    if len(user_input_split[-1]) == 16 or len(user_input_split[-1]) == 15:
        return f"{type_user_card} {get_mask_card_number(int(user_input_split[-1]))}"
    elif len(user_input_split[-1]) == 20 or len(user_input_split[-1]) == 19:
        return f"{type_user_card} {get_mask_account(int(user_input_split[-1]))}"
    else:
        raise ValueError("Введенного номера не существует")


def get_date(date: str) -> datetime:
    """Функция, которая преобразует дату в формат ДД.ММ.ГГГГ"""
    date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


# user_input = input("Введите данные карты или счета: ")
# print(mask_account_card(user_input))
# user_date = input("Введите дату: ")
# print(get_date("2019-07-03T18:35:29.512364"))
