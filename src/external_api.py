import os
import json

import requests
from dotenv import load_dotenv

load_dotenv("../ .env")
# Загружаем переменные окружения из .env

API_KEY = os.getenv("API_KEY")
# Получаем токен доступа из переменных окружения

r = requests.get('https://apilayer.com/exchangerates_data-api')

def converter(transaction: dict):
    """Реализуем функцию, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли"""
    amount = transaction ["operationAmount"]["amount"]
    currency = transaction ["operationAmount"]["currency"]["code"]
    if transaction ["operationAmount"]["currency"]["code"] == "RUB":
        return amount
    else:
        headers = {'apikey": 4mLARB2HnFEgAB7cdhgi40Y498sxzP7a'}

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}/&amount={amount}"
        response = requests.get(url, headers=headers)
        status_code = response.status_code
        if status_code != 200:
            print(response.reason)
        else:
            result = response.json()
            data = result.get("result")
            return data

