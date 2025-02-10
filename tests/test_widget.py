import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize('input_data, expected_output', [
    ('Visa Platinum 700079228960636', 'Visa Platinum 7000 ** **** 0636'),
    ('Счет 73654108430135874305', 'Счет ***************4305'),
    ('', 'Неверный формат ввода'),
    ('Сч', 'Неверная длина номера счета для маскирования.'),
    ('Счет 123', 'Номер карты должен быть длиной 16 символов для маскирования.'),
])
def test_mask_account_card(input_data, expected_output):
    with pytest.raises(ValueError):
        mask_account_card(input_data)

'''@pytest.mark.parametrize('input_mask, output_mask', [
    ('Visa Platinum 700079228960636', 'Visa Platinum 7000 79** **** 0636'),
    ('Счет 73654108430135874305', 'Счет **4305'),
    ('', 'Неверный формат ввода')
])
def test_mask_account_card(input_mask, output_mask):
    assert mask_account_card(input_mask) == output_mask

@pytest.mark.parametrize('input_mask, output_mask', [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('', 'Неверный формат даты')
])
def test_get_date(input_mask, output_mask):
    assert get_date(input_mask) == output_mask'''
