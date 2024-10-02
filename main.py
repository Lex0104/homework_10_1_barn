from src.processing import filter_by_state, sort_by_date
from src.widget import get_data, mask_account_card

print(mask_account_card("MasterCard 7158300734726758"))

print(mask_accoun4t_card("Счет 35383033474447895560"))

print(get_data("2024-03-11T02:26:18.671407"))

print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]
    )
)

print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]
    )
)
