from unittest.mock import patch
from src.external_api import converter
import requests


@patch('requests.get')
def test_converter(mock_get):
    mock_get.return_value.json.return_value = {
   "date": "2024-10-22",
    "id": "587085106",
    "name": "доллар",
    "code": "USD"
}

    assert converter == {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
        }
    }
}
