# from src.generators import transaction_descriptions, card_number_generator, filter_by_currency
# from src.decorators import log
# from src.dictionary_search import dict_search_bank, number_operations
import os
from src.utils import get_financial_transactions_data
from src.transactions_csv_excel import transactions_csv, transactions_xlsx


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def main():
    work_file = input(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями. "
        "\nВыберите необходимый пункт меню: "
        "\n1.Получить информацию о транзакциях из JSON-файла"
        "\n2.Получить информацию о транзакциях из CSV-файла"
        "\n3.Получить информацию о транзакциях из XLSX-файла"
        "\nВвод: "
    ).strip()
    while True:
        if work_file == "1":
            print("Для обработки выбран JSON-файл")
            return get_financial_transactions_data(os.path.join(os.path.dirname(__file__), "data", "operations.json"))
            break
        elif work_file == "2":
            print("Для обработки выбран CSV-файл")
            return transactions_csv((os.path.join(os.path.dirname(__file__), "data", "transactions.csv")))
            break
        elif work_file == "3":
            print("Для обработки выбран XLSX-файл")
            return transactions_xlsx((os.path.join(os.path.dirname(__file__), "data", "transactions_excel.xlsx")))
            break
        else:
            input("Данного варианта нет в списке, попробуйте еще раз:\nВвод: ")

            status_operation = (
                input(
                    "\nВведите статус, по которому необходимо выполнить фильтрацию. "
                    "\nДоступные для фильтровки статусы: "
                    "EXECUTED, CANCELED, PENDING:\nВвод: "
                )
                .strip()
                .upper()
            )

            while True:
                if status_operation == "PENDING" or status_operation == "EXECUTED" or status_operation == "CANCELED":
                    status_operation = (
                        input(
                            f"Статус {status_operation} не доступен.\n"
                            "\nВведите статус, по которому необходимо выполнить фильтрацию."
                            "\nДоступные для фильтровки статусы: "
                            "EXECUTED, CANCELED, PENDING:\nВвод: "
                        )
                        .strip()
                        .upper()
                    )

        print("Отсортировать операции по дате? Да/Нет")
        user_client = input("Введите да или нет ").lower()
        if user_client == "Да":
            print("Отсортировать по возростанию или по убыванию?")
        user_client_down = input("В порядке убывания/ В порядке возрастания").lower()
        if user_client_down == " В порядке возрастания":
            print("Выводить только рублевые транзакции? Да/Нет")
        user_like_rub = input("Введите да или нет ").lower()
        if user_like_rub == "Да":
            print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_transactions = input("Введите да или нет ").lower()
        if user_transactions == "Да":
            print("Распечатываю итоговый список транзакций...")
        result(data)


if __name__ == "__main__":
    main()
