import os
from src.setup_logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "./logs", "masks.log")
logger = setup_logger("masks", file_path_1)

def get_mask_card_number(user_card_number: str) -> str:
    """Функция принимает строку и возвращает номер карты пользователя"""

    logger.info(f"задаём формат маски для номера банковской карты {user_card_number}")
    new_string = f"{user_card_number[0:4]} {user_card_number[4:6]}** **** {user_card_number[12:]}"
    return new_string


def get_mask_account(account_number: str) -> str:
    """Функция принимает строку и возвращает маску счета"""

    logger.info(f"Проверяем правильность написания {account_number}")
    if len(str(account_number)) != 20:
        logger.error("Ошибка. Проверьте номер счета, он должен содержать 20 цифр")
        raise ValueError ("Проверьте номер счета, он должен содержать 20 цифр ")
    else:
        logger.info(f"Задаём формат маски для номера бавковского счета {account_number}")
        account_with_masks = account_number.replace(account_number[:-4], "*" * 2)

    return account_with_masks
