# from src.generators import transaction_descriptions, card_number_generator, filter_by_currency
# from src.decorators import log
# from src.dictionary_search import dict_search_bank, number_operations
import os
from src.utils import get_financial_transactions_data
from src.transactions_csv_excel import transactions_csv, transactions_xlsx
from src.proccessing import sort_by_date, filter_by_state
from src.dictionary_search import dict_search_bank
from src.widget import mask_account_card, get_data
from src.generators import filter_by_currency


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


def main_1():
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

            # status_operation = (
            #     input(
            #         "\nВведите статус, по которому необходимо выполнить фильтрацию. "
            #         "\nДоступные для фильтровки статусы: "
            #         "EXECUTED, CANCELED, PENDING:\nВвод: "
            #     )
            #     .strip()
            #     .upper()
            # )
            #
            # while True:
            #     if status_operation == "PENDING" or status_operation == "EXECUTED" or status_operation == "CANCELED":
            #         status_operation = (
            #             input(
            #                 f"Статус {status_operation} не доступен.\n"
            #                 "\nВведите статус, по которому необходимо выполнить фильтрацию."
            #                 "\nДоступные для фильтровки статусы: "
            #                 "EXECUTED, CANCELED, PENDING:\nВвод: "
            #             )
            #             .strip()
            #             .upper()
            #         )


def choice_state(data: list) -> list:
    """Фильтрация данных по выбранному статусу"""
    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию."
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        user_input_2 = input()
        if (
                user_input_2.upper() != "EXECUTED"
                and user_input_2.upper() != "CANCELED"
                and user_input_2.upper() != "PENDING"
        ):
            print(f'Статус операции "{user_input_2}" недоступен')
        else:
            print(f'Операции отфильтрованы по статусу "{user_input_2}"')
            data = filter_by_state(data, user_input_2.upper())
            break
    return data


def choice_sort_date(data: list) -> list:
    """Сортировка по дате"""
    user_sort = input()
    if user_sort.lower() == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        sort_up_or_lower = input()
        if sort_up_or_lower.lower() == "по возрастанию":
            is_reverse = False
            data = sort_by_date(data, is_reverse)
        else:
            is_reverse = True
            data = sort_by_date(data, is_reverse)
        return data


def sort_rub(data: list) -> list:
    """Фильтрация по рублевым транзакциям"""
    rub_transaction = input()
    if rub_transaction.lower() == "да":
        data = filter_by_currency(data, "RUB")
    return list(data)


def sort_word(data: list, sort_by_word: str) -> list:
    """Фильтрация по строке"""
    if sort_by_word.lower() == "да":
        print("Введите слово:")
        string_to_search = input()
        data = dict_search_bank(data, string_to_search)
    return data


def final_result(data: list) -> None:
    """Вычисление и вывод результатов по полученному списку транзакций"""
    global mask_to
    if len(data) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(data)}\n")

        for transaction in data:
            date = get_data(transaction.get("date"))

            try:
                mask_from = mask_account_card(transaction["from"])
                print(f"{date} {transaction} {mask_from} -> ", end="")
            except KeyError:
                print(f"{date} {transaction} ", end="")
            except KeyError:
                print(f"{date} {transaction}", end="")

                mask_to = mask_account_card(transaction["to"])
            try:
                amount = transaction["amount"]
            except KeyError:
                amount = transaction["operationAmount"]["amount"]
            try:
                currency = transaction["currency_name"]
            except KeyError:
                currency = transaction["operationAmount"]["currency"]["name"]
            print(f"{mask_to} Сумма: {amount} {currency}")


def main() -> None:
    """Возвращает список транзакций по выбранным условиям"""
    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""
    )
    data = main_1()
    data = choice_state(data)
    print("Отсортировать операции по дате? Да/Нет")
    data = choice_sort_date(data)
    print("Выводить только рублевые транзакции? Да/Нет")
    data = sort_rub(data)
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    sort_by_word = input()
    data = sort_word(data, sort_by_word)
    print("Распечатываю итоговый список транзакций...")
    final_result(data)


if __name__ == "__main__":
    main()

