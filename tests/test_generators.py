import pytest
from src.generators import transaction_descriptions,  filter_by_currency, card_number_generator


def test_filter_by_currency_empty_list() -> None:
    """Тест проверяет, что функция filter_by_currency корректно
    работает при передаче ей пустого списка и не завершается
    ошибкой после окончания работы генератора"""
    empty_transaction = filter_by_currency([])
    assert next(empty_transaction) == "Пустой список транзакций"
    assert next(empty_transaction) == "Генератор закончил работу"

def test_filter_by_no_currency_in_list(transactions_for_generate: list, currency: str = "EURO") -> None:
    """Тест проверяет, что функция-генератор filter_by_currency корректно
    работает при передаче ей списка, где нет заданной валюты"""
    no_necessary_transaction = filter_by_currency(transactions_for_generate, currency)
    assert next(no_necessary_transaction) == "Транзакции в заданной валюте отсутствуют"
    assert next(no_necessary_transaction) == "Генератор закончил работу"

@pytest.mark.parametrize(
    "expected",
    [
        (
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод со счета на счет",
                "Перевод с карты на карту"
                "Перевод организации"
            ]
        )
    ])
def test_transaction_descriptions(transactions_for_generate: list, expected: str) -> str:
    """Тест проверяет работу генератора transaction_descriptions"""
    transactions = transaction_descriptions(transactions_for_generate)
    for index in range(6):
        assert next(descriptions) == expected[index]

    assert next(descriptions) == "Генератор закончил работу"


def test_no_transaction_descriptions(transactions_for_generate: list) -> str:
    """Тест проверяет работу функции-генератора transaction_descriptions при передаче
    ей пустого списка"""
    descriptions = transaction_descriptions([])
    assert next(descriptions) == "Пустой список транзакций"
    assert next(descriptions) == "Генератор закончил работу"



def test_card_number_generator(start: int, stop: int, expected: list) -> None:
    """Тест проверяет работу функции-генератора card_number_generator"""
    card_number = card_number_generator(start, stop)

    for index in range(stop - start + 1):
        assert next(card_number) == expected[index]


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (-1, 10, "Диапазон чисел меньше 0"),
        (10, -1, "Диапазон чисел меньше 0"),
        (1, 1, "Начало и конец диапазона совпадают"),
        (999999999999999, 99999999999999999, "Диапазон чисел вышел за верхнюю границу"),
    ],
)
def test_card_number_generator_wrong_cases(start: int, stop: int, expected: list) -> None:
    """Проверяет работу функции-генератора card_number_generator,
    когда на вход были переданы неверные данные"""
    card_number = card_number_generator(start, stop)
    assert next(card_number) == expected