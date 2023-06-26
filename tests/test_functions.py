import pytest
from utils.functions import get_data, filtered_data, get_formatted_data, encode_bill_info

def test_get_data():
    data = get_data('utils/test_1.json')
    assert isinstance(data, list)

def test_filtered_data(test_data):
    date = filtered_data(test_data)
    assert len(date) == 5

def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ['26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.', '03.07.2019 Перевод организации\nMasterCard 7158 30** **** 6758 -> Счет **5560\n8221.37 USD', '30.06.2018 Перевод организации\nСчет **6952 -> Счет **6702\n9824.07 USD', '23.03.2018 Открытие вклада\nСчет **2431\n48223.05 руб.', '04.04.2019 Перевод со счета на счет\nСчет **8542 -> Счет **4188\n79114.93 USD', '23.03.2019 Перевод со счета на счет\nСчет **4719 -> Счет **1160\n43318.34 руб.']

@pytest.mark.parametrize("test_input, expected", [
    ("Счет 46363668439560358409", "Счет **8409"),
    ("МИР 8326537236216459", "МИР 8326 53** **** 6459")
])
def test_encode_bill_info(test_input, expected):
    assert encode_bill_info(test_input) == expected