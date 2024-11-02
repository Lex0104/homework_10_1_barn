import csv
import pandas as pd
import os


def transactions_csv(path: str) -> list:
    """Чтение csv файла"""
    with open(path) as file:
        transaction_list = []
        py_file = csv.DictReader(file, delimiter=";")
        for row in py_file:
            transaction_list.append(row)
        return transaction_list


print(transactions_csv(os.path.join(os.path.dirname(__file__), "data", "transactions.csv")))


def transactions_xlsx(path) -> list[dict]:
    """Чтение excel файла"""
    py_from_xlsx = pd.read_excel(path)
    py_dict = py_from_xlsx.to_dict(orient="records")
    return py_dict


print(transactions_xlsx(os.path.join(os.path.dirname(__file__), "data", "transactions_excel.xlsx")))
