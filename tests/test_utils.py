import json
import requests
from unittest.mock import MagicMock,patch
from src.utils import get_financial_transactions_data

@patch('transcations')
def get_financial_transactions_data(mock_open: MagicMock, path_name:patch, mock_file=None) -> None:
    mock_file.read.return_value = json.dumps([{"id": 441945886}])
    assert get_financial_transactions_data(path_name) == ([{"id": 441945886}])
