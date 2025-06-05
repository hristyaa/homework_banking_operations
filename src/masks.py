def get_mask_card_number(card_number: int) -> str:
    """Функция, которая возвращает маску номера карты  по правилу XXXX XX** **** XXXX"""
    if len(str(card_number)) == 16:  # проверка номера карта на правильность по количеству символов
        mask_card_number = str(card_number)[:4] + " " + str(card_number)[4:6] + "** **** " + str(card_number)[-4:]
        return mask_card_number
    else:
        return "Введенного номера карты не существует"


def get_mask_account(account_number: int) -> str:
    """Функция, которая возвращает маску номера счета пользователя по правилу **XXXX"""
    if len(str(account_number)) == 20:  # проверка номера счета на правильность по количеству символов
        return "**" + str(account_number)[-4:]
    else:
        return "Введенного номера счета не существует"

#user_card_number = int(input("Введите номер карты: "))
get_mask_card_number(7000792289606361)
#user_account_number = int(input("Введите номер cчета: "))
get_mask_account(73654108430135874305)
