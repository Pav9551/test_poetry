from src.masks import get_mask_card_number, get_mask_account
from src.processing import filter_by_state, sort_by_date

# Вывод функций
if __name__ == '__main__':
    print(get_mask_card_number('7000792289606361'))
    print(get_mask_account('73654108430135874305'))

from src.widget import mask_account_card, get_date

# Вывод функций
if __name__ == '__main__':
    print(mask_account_card('Maestro 1596837868705199'))
    print(mask_account_card('Счет 64686473678894779589'))
    print(get_date('2024-03-11T02:26:18.671407'))


# Вывод функций
if __name__ == '__main__':
    print(
        filter_by_state(
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
            ]
        )
    )

if __name__ == '__main__':
    print(
        sort_by_date(
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
            ]
        )
    )


if __name__ == '__main__':
    print(get_mask_card_number('524859756321548759'))
