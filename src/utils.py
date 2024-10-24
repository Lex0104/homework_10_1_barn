import json
import os
from typing import Any
from src.setup_logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "./logs", "utils.log")
logger = setup_logger("utils", file_path_1)

def get_financial_transactions_data(file_path: str) -> Any:
    empty_list = []
    with open(file_path, 'r', encoding="utf-8") as file:
        try:
            logger.info(f"0ткрытие json файла{file_path}")
            transactions = json.load(file)
            logger.info ( f"Проверяем, что файл{file_path} не пустой" )
            if transactions == 0 or type(transactions) != list:
                return empty_list
            else:
                logger.info(f"Возвращаем пустой словарь, если файл{file_path} пустой")
                return transactions
        except Exception:
            logger.error("Ошибка")
            print ("Invalid JSON data.")
            return empty_list


if __name__ == "__main__":
    file_to_path = (os.path.join(os.path.dirname(__file__), "data", "operations.json"))







