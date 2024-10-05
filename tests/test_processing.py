import pytest

from src.processing import filter_by_state, sort_by_date

def test_filter_by_state(list):
    assert filter_by_state(list) == [
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
    ]

def test_filter_by_state():
    assert filter_by_state ( [] ) == []

@pytest.mark.parametrize(
    "list_dict, direction, sorted_list" (
        [
            (
                    [
                        {
                            "id" : 41428829,
                            "state" : "EXECUTED",
                            "date" : "2019-07-03T18:35:29.512364",
                        },
                        {
                            "id" : 939719570,
                            "state" : "EXECUTED",
                            "date" : "2018-06-30T02:08:58.425572",
                        }
                    ]
            )
        ]
)


def test_get_sort_list_date(list_dict, direction, sorted_list):
    assert get_sort_list_date(list_dict, direction) == sorted_list