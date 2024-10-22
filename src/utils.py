import json
import os
from typing import Any

def get_financial_transactions_data(file_path: str) -> Any:
    empty_list = []
    with open(file_path, 'r', encoding="utf-8") as file:
        try:
            transactions = json.load(file)
            if transactions == 0 or type(transactions) != list:
                return empty_list
            else:
                return transactions
        except json.JSONDecodeError:
            print ("Invalid JSON data.")
            return empty_list


if __name__ == "__main__":
    file_to_path = (os.path.join(os.path.dirname(__file__), "data", "operations.json"))







