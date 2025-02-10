import pytest
from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number() -> None:
    """Тест на правильность маскирования номера карты"""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"

def test_get_mask_account() -> None:
    """Тест на правильность маскирования номера счета"""
    assert get_mask_account("7000792289606361") == "************6361"

def test_get_mask_account_invalid_length() -> None:
    """Проверка работы функции на нестандартные длины номеров счетов."""
    with pytest.raises(ValueError, match="Неверная длина номера счета."):
        get_mask_account("73654108430135874305")
