import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def filter_by_currency(transactions):
    filter_currency = filter_by_currency(transactions, "USD")
    assert next(filter_currency) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Cчет 75106830613057916952",
        "to": "Счет 11776014605903060702",
    }


def transaction_descriptions(transactions):
    transactions_descrt = transaction_descriptions(transactions)
    assert next(transactions_descrt) == "Перевод организации"
    assert next(transactions_descrt) == "Перевод со счета на счет"
    assert next(transactions_descrt) == "Перевод со счета на счет"
    assert next(transactions_descrt) == "Перевод с карты на карту"
    assert next(transactions_descrt) == "Перевод организации"


def test_card_number_generator() -> None:
    generator = card_number_generator(1, 6)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"
