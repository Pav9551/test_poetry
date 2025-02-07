from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(to_mask: str = "") -> str:
    """Функция, которая принимает имя и номер карты и возвращает маску"""
    if "Счет" in to_mask:
        return "Счет" + get_mask_account(to_mask)
    else:
        cards = get_mask_card_number(to_mask[-16:])
        new_card = to_mask.replace(to_mask[-16:], cards)
        return new_card


def get_date(take_the_date: str) -> str:
    """Функция, которая возвращает дату в другом формате"""
    new_date = take_the_date.split("T")
    date = new_date[0].split("-")
    return (f"{date[-1]}.{date[-2]}.{date[-3]}")
