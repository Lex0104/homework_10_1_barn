def get_mask_card_number(user_card_number: str) -> str:
    """Функция принимает строку и возвращает номер карты пользователя"""
    new_string = f"{user_card_number[0:4]} {user_card_number[4:6]}** **** {user_card_number[12:]}"
    return new_string


def get_mask_account(account_number: str) -> str:
    """Функция принимает строку и возвращает маску счета"""
    new_mask = f"**{account_number[-4:]}"
    return new_mask
