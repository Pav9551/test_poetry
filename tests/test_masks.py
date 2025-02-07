import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number() -> None:
    """Тест на правильность маскирования номера карты"""
    assert get_mask_card_number("7000792289606361") == "7000 22** **** 6361"

def test_get_mask_account() -> None:
    """Тест на правильность маскирования номера счета"""
    assert get_mask_account("73654108430135874305") == "**4305"

with pytest.raises(ValueError):
    """Проверка работы функции на нестандартные длины номеров карт"""
    get_mask_card_number(52013597452142)

with pytest.raises(ValueError):
    """Проверка работы функции на нестандартные длины номеров счетов"""
    get_mask_account(736541084301358743)
