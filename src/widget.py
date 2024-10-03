from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(number_string: str) -> str:
    """Функция принимает строку и маскирует номер карты и счета"""
    if len(number_string.split()[-1]) == 16:
        new_masks_account = get_mask_card_number(number_string.split()[-1])
        result = f"{number_string[:-16]}{new_masks_account}"
        return result
    elif len(number_string.split()[-1]) == 20:
        new_masks_account = get_mask_account(number_string.split()[-1])
        result = f"{number_string[:-20]}{new_masks_account}"
    return result


def get_data(old_data: str) -> str:
    """Функция принимает на вход строку с датой в формате и форматирует её"""
    new_data = old_data[0:10].split("-")
    return ".".join(new_data[::-1])
