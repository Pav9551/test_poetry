import pytest
from src.processing import filter_by_state, sort_by_date
from typing import Dict, List

def test_filter_by_state_executed(expected_filter_by_state_executed: List[Dict]) -> None:
    assert filter_by_state(expected_filter_by_state_executed) == expected_filter_by_state_executed

def test_filter_by_state_canceled(expected_filter_by_state_canceled: List[Dict]) -> None:
    """Тестирование фильтрации списка словарей по заданному статусу state"""
    assert filter_by_state(expected_filter_by_state_canceled, state: "CANCELED") == expected_filter_by_state_canceled

def test_filter_by_state_zero(expected_filter_by_state_zero: List[Dict]) -> None:
    """Проверка работы функции при отсутствии словарей с указанным статусом"""
    assert filter_by_state(expected_filter_by_state_zero) == expected_filter_by_state_zero

def test_sort_by_date(expected_sort_by_date: List[Dict]) -> None:
    assert sort_by_date(expected_sort_by_date) == expected_sort_by_date

def test_sort_by_date_false(expected_sort_by_date_false: List[Dict]) -> None:
    assert sort_by_date(expected_sort_by_date_false, reverse: False) == expected_sort_by_date_false





