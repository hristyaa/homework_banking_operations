import logging
import os

mask_logger = logging.getLogger("app.masks")

log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "logs"))
os.makedirs(log_dir, exist_ok=True)

file_handler = logging.FileHandler(filename=os.path.join(log_dir, "masks.log"), mode="w", encoding="utf-8")

file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

mask_logger.addHandler(file_handler)
mask_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """Функция, которая возвращает маску номера карты  по правилу XXXX XX** **** XXXX"""
    mask_logger.info("Проверка номера карта на правильность по количеству символов")
    if len(str(card_number)) == 16 or len(str(card_number)) == 15:  # проверка номера карта на правильность по количеству символов
        mask_logger.info("Маскировка номера карты")
        mask_card_number = str(card_number)[:4] + " " + str(card_number)[4:6] + "** **** " + str(card_number)[-4:]
        return mask_card_number
    else:
        mask_logger.error("Произошла ошибка, введенного номера карты не существует")
        raise ValueError("Введенного номера карты не существует")


def get_mask_account(account_number: int) -> str:
    """Функция, которая возвращает маску номера счета пользователя по правилу **XXXX"""
    mask_logger.info("Проверка номера счета на правильность по количеству символов")
    if len(str(account_number)) == 20 or len(str(account_number)) == 19:  # проверка номера счета на правильность по количеству символов
        mask_logger.info("Маскировка номера счета")
        return "**" + str(account_number)[-4:]
    else:
        mask_logger.error("Произошла ошибка,введенного номера счета не существует ")
        raise ValueError("Введенного номера счета не существует")


# user_card_number = int(input("Введите номер карты: "))
# get_mask_card_number(user_card_number)
# get_mask_card_number(7000792289606361)
# user_account_number = int(input("Введите номер cчета: "))
# get_mask_account(user_account_number)
# get_mask_account(73654108430135874305)
# get_mask_card_number(123451245)
# get_mask_account("123abc")
