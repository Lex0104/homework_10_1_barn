from src.generators import transaction_descriptions, card_number_generator, filter_by_currency
from src.decorators import log
from src.dictionary_search import dict_search_bank, number_operations

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


usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(3):
    print(next(usd_transactions)["id"])


descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))


for card_number in card_number_generator(1, 5):
    print(card_number)


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)


@log(filename="mylog.txt")
def my_function_zero_error(x, y):
    return x / y


my_function_zero_error(3, 0)


json_file_path = os.path.join("data", "operations. json")
transactions = get_list_transactions(json_file_path.py)
print(transactions)

for transaction in transactions:
    rub_amount = amount(transaction)
    print(f"Транзакция в RUB: {rub_amount}")


def main():
    work_file = input(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями. "
        "\nВыберите необходимый пункт меню: "
        "\n1.Получить информацию о транзакциях из JSON-файла"
        "\n2.Получить информацию о транзакциях из CSV-файла"
        "\n3.Получить информацию о транзакциях из XLSX-файла"
        "\nВвод: ").strip()
    while True:
        if work_file == "1":
            print("Для обработки выбран JSON-файл")
            read_file = read_file_json(os.path.join(os.path.dirname(__file__), "data/operations.json"))
            break
        elif work_file == "2":
            print("Для обработки выбран CSV-файл")
            read_file = read_file_csv(os.path.join(os.path.dirname(__file__), "data/transactions.csv"))
            break
        elif work_file == "3":
            print("Для обработки выбран XLSX-файл")
            read_file = read_file_excel(os.path.join(os.path.dirname(__file__), "data/transactions_excel.xlsx"))
            break
        else:
            work_file = input("Данного варианта нет в списке, попробуйте еще раз:\nВвод: ")

        choice_state= input("\nВведите статус, по которому необходимо выполнить фильтрацию. "
                             "\nДоступные для фильтровки статусы: "
                             "EXECUTED, CANCELED, PENDING:\nВвод: ").strip().upper()

    data = file_selection ()
    data = choice_state(data)
    print ( "Отсортировать операции по дате? Да/Нет" )
    data = choice_sort_by_date(data)
    print ( "Выводить только рублевые транзакции? Да/Нет")
    data = sort_by_rub(data)
    print ( "Отфильтровать список транзакций по определенному слову в описании? Да/Нет" )
    sort_by_word = input ()
    data = filter_by_world(data, sort_by_word)
    print ( "Распечатываю итоговый список транзакций..." )
    result (data)


if __name__ == "__main__" :
    main ()

