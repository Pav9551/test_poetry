from typing import Dict, List, Union


def filter_by_state(
        data_list: List[Dict[str, Union[str, int]]], state: str = "EXECUTED") -> List[Dict[str, Union[str, int]]]:
    """Функция, которая фильтрует список словарей по значению ключа state"""
    return [item for item in data_list if item.get("state") == state]


def sort_by_date(
        data_list: List[Dict[str, Union[str, int]]], reverse: bool = True) -> List[Dict[str, Union[str, int]]]:
    """Функция, которая возвращает новый список, отсортированный по дате"""
    return sorted(data_list, key=lambda x: x["date"], reverse=reverse)
