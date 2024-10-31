from src.dictionary_search import dict_search_bank, number_operations


def test_dict_search_bank(operations: list) -> None:
    assert dict_search_bank(operations, "CANCELED") == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "currency": {"name": "руб.", "code": "RUB"},
                "amount": "31957.58",
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            },
        }
    ]


def test_number_operations(operations: list) -> None:
    assert number_operations(operations, ["Перевод со счета на счет"]) == {"Перевод со счета на счет": 2}
