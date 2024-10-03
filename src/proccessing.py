
def filter_by_state(list_of_dict: list, state: int = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, у которых ключ state соответствует указанному значению"""
    filtred_list = []
    for ld in list_of_dict:
        if ld.get("state") == state:
            filtred_list.append(ld)
    return filtred_list


def sort_by_date(list_dict: list, direction: bool = True) -> list:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание"""
    sorted_list = sorted(list_dict, key=lambda x: ["date"], reverse=direction)
    return sorted_list


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]
    )
)

def filter_by_state(list_dict: list, state: int = "EXECUTED") -> int:
    """Функция возвращает новый список словарей, у которых ключ state соответствует указанному значению"""
    filtred_list = []
    for ld in list_dict:
        if ld.get("state") == state:
            filtred_list.append(ld)
    return filtred_list


def sort_by_date(list_dict: list) -> int:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание"""
    sorted_list = sorted(list_dict, key=lambda x: ["date"])
    return sorted_list

print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]
    )
)

