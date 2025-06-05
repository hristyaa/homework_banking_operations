from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(user_input: str) -> str:
    """Функция, которая возвращает замаскированный номер карты или счета"""
    user_input_split = user_input.split(' ')   #разделение введенных данных по пробелам
    type_user_card = " ".join(user_input_split[0:-1])  #занесение в переменную тип карты/счет
    if len(user_input_split[-1]) == 16:
        return f"{type_user_card} {get_mask_card_number(int(user_input_split[-1]))}"
    if len(user_input_split[-1]) == 20:
        return f"{type_user_card} {get_mask_account(int(user_input_split[-1]))}"


user_input = input('Введите данные карты или счета: ')
print(mask_account_card(user_input))
