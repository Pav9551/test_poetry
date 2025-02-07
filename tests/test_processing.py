import pytest
from src.processing import filter_by_state, sort_by_date
from typing import Dict, List

@pytest.fixture
def sample_transactions() -> List[Dict]:
    """Пример списка транзакций для тестирования"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-05T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2023-01-03T14:30:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-04T09:15:00"}
    ]

@pytest.fixture
def expected_filter_by_state_executed() -> List[Dict]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-05T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-04T09:15:00"}
    ]

@pytest.fixture
def expected_filter_by_state_canceled() -> List[Dict]:
    return [
        {"id": 2, "state": "CANCELED", "date": "2023-01-03T14:30:00"}
    ]

@pytest.fixture
def expected_sort_by_date() -> List[Dict]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-05T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-04T09:15:00"},
        {"id": 2, "state": "CANCELED", "date": "2023-01-03T14:30:00"}
    ]

@pytest.fixture
def expected_sort_by_date_false() -> List[Dict]:
    return [
        {"id": 2, "state": "CANCELED", "date": "2023-01-03T14:30:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-04T09:15:00"},
        {"id": 1, "state": "EXECUTED", "date": "2023-01-05T12:00:00"}
    ]

def test_filter_by_state_executed(sample_transactions, expected_filter_by_state_executed) -> None:
    assert filter_by_state(sample_transactions, state="EXECUTED") == expected_filter_by_state_executed

def test_filter_by_state_canceled(sample_transactions, expected_filter_by_state_canceled) -> None:
    """Тестирование фильтрации списка словарей по заданному статусу state"""
    assert filter_by_state(sample_transactions, state="CANCELED") == expected_filter_by_state_canceled

def test_filter_by_state_zero(sample_transactions) -> None:
    """Проверка работы функции при отсутствии словарей с указанным статусом"""
    assert filter_by_state(sample_transactions, state="PENDING") == []

def test_sort_by_date(sample_transactions, expected_sort_by_date) -> None:
    assert sort_by_date(sample_transactions) == expected_sort_by_date

def test_sort_by_date_false(sample_transactions, expected_sort_by_date_false) -> None:
    assert sort_by_date(sample_transactions, reverse=False) == expected_sort_by_date_false
