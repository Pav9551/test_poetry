import pytest
from src.generators import transaction_description, filter_by_currency, card_number_generator
@pytest.fixture
def transactions_for_generate():
    return [
        {"amount": 100, "currency": "USD", "description": "Перевод"},
        {"amount": 200, "currency": "RUB", "description": "Оплата"},
    ]
def test_filter_by_currency_empty_list() -> None:
    """Test that filter_by_currency correctly handles an empty transaction list."""
    empty_transaction = filter_by_currency([])
    assert next(empty_transaction) == "Пустой список транзакций"
    with pytest.raises(StopIteration):
        next(empty_transaction)

def test_filter_by_no_currency_in_list(transactions_for_generate: list, currency: str = "EURO") -> None:
    """Test that filter_by_currency correctly handles when no transactions match the specified currency."""
    no_necessary_transaction = filter_by_currency(transactions_for_generate, currency)
    assert next(no_necessary_transaction) == "Транзакции в заданной валюте отсутствуют"
    with pytest.raises(StopIteration):
        next(no_necessary_transaction)

@pytest.mark.parametrize(
    "transactions_for_generate, expected",
    [
        (
            [
                {"description": "Перевод организации"},
                {"description": "Перевод со счета на счет"},
                {"description": "Перевод со счета на счет"},
                {"description": "Перевод с карты на карту"},
                {"description": "Перевод организации"}
            ],
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Перевод организации"
            ]
        )
    ]
)
def test_transaction_description(transactions_for_generate: list, expected: list) -> None:
    """Test the generator transaction_description for expected output."""
    transactions = transaction_description(transactions_for_generate)
    for index, expected_description in enumerate(expected):
        assert next(transactions) == expected_description
    with pytest.raises(StopIteration):
        next(transactions)

def test_no_transaction_descriptions() -> None:
    """Test transaction_description with an empty list."""
    descriptions = transaction_description([])
    assert next(descriptions) == "Пустой список транзакций"
    with pytest.raises(StopIteration):
        next(descriptions)

def test_card_number_generator() -> None:
    """Test the card_number_generator function."""
    expected = ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]  # example expected
    start, stop = 1, 3
    card_number = card_number_generator(start, stop)
    for index in range(stop - start + 1):
        assert next(card_number) == expected[index]
    with pytest.raises(StopIteration):
        next(card_number)

@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (-1, 10, "Число должно быть в диапазоне от 1 до 9999 9999 9999 9999"),
        (10, -1, "Первое число не может быть больше второго"),
        (1, 1, "0000 0000 0000 0001"),
        (9999999999999999, 10000000000000000, "Число должно быть в диапазоне от 1 до 9999 9999 9999 9999"),
    ]
)
def test_card_number_generator_wrong_cases(start: int, stop: int, expected: str) -> None:
    """Test card_number_generator for various erroneous inputs."""
    card_number = card_number_generator(start, stop)
    assert next(card_number) == expected
    if expected.startswith("Число должно быть"):
        with pytest.raises(StopIteration):
            next(card_number)
