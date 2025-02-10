from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(to_mask: str = "") -> str:
    """Функция, маскирующая номер счета или карты в заданной строке."""
    if "Счет" in to_mask:
        # Предположим, что номер счета идет сразу после "Счет" и имеет длину 20
        # Это можно подстроить под ваш конкретный случай (например, поиск по регулярному выражению)
        account_number = to_mask.split("Счет")[-1].strip()
        if len(account_number) < 4:
            # Минимальная разумная длина, выполняем дополнительную валидацию
            raise ValueError("Неверная длина номера счета для маскирования.")
        return "Счет " + get_mask_account(account_number)
    else:
        # Здесь предполагаем, что карта находится в конце строки и имеет длину 16
        card_number = to_mask[-16:].strip()
        if len(card_number) != 16:
            raise ValueError("Номер карты должен быть длиной 16 символов для маскирования.")
        cards = get_mask_card_number(card_number)
        new_card = to_mask.replace(card_number, cards)
        return new_card

def get_date(take_the_date: str) -> str:
    """Функция, которая переворачивает дату из формата ГГГГ-ММ-ДД в формат ДД.ММ.ГГГГ."""
    try:
        new_date = take_the_date.split("T")[0]
        date_parts = new_date.split("-")
        if len(date_parts) != 3:
            raise ValueError("Неверный формат даты.")
        # Проверка, что все части даты являются числами
        year, month, day = date_parts
        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            raise ValueError("Дата должна содержать только числа.")
        return f"{day.zfill(2)}.{month.zfill(2)}.{year}"
    except Exception as e:
        return f"Ошибка обработки даты: {str(e)}"
