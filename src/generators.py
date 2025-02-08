from gettext import translation
from typing import Any, Iterator
# Исправленный список транзакций
transactions_list = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }
]

def filter_by_currency(transactions_list: list, currency: str = "USD") -> Iterator[Any]:
    """Фильтрует транзакции по заданной валюте"""
    amount_transactions = 0

    if not transactions_list:
        yield "Пустой список транзакций"
        return

    for transaction in transactions_list:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            amount_transactions += 1
            yield transaction

    if amount_transactions == 0:
        yield "Транзакции в заданной валюте отсутствуют"

def transaction_description(transactions_list: list) -> Iterator[str]:
    """Возвращает описание каждой операции по очереди"""
    if not transactions_list:
        yield "Пустой список транзакций"
        return

    for transaction in transactions_list:
        yield transaction["description"]



def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генерирует номера карт в заданном диапазоне"""

    # Проверяем, что start не больше stop
    if start > stop:
        yield "Первое число не может быть больше второго"
        return

    # Проверяем, что числа в допустимом диапазоне
    if not (1 <= start <= 9999999999999999 and 1 <= stop <= 9999999999999999):
        yield "Число должно быть в диапазоне от 1 до 9999 9999 9999 9999"
        return

    # Генерация номеров карт
    while start <= stop:
        card_number = str(start).zfill(16)  # Добавляем ведущие нули
        formatted_card_number = " ".join([card_number[i:i+4] for i in range(0, 16, 4)])
        yield formatted_card_number
        start += 1
