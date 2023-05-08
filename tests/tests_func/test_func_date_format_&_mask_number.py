import pytest

from src.func import data_format, mask_nuber


@pytest.fixture
def data():
    """Тестовые данные"""
    return [
        {
            "date": "2019-07-03T18:35:29.512364",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
            "description": "Перевод организации",
            "operationAmount": {"amount": 1000.0, "currency": {"name": "USD"}}
        },
        {
            "date": "2018-03-23T10:45:06.972075",
            "from": "Счет 1234567890",
            "to": "Счет 75651667383060284188",
            "description": "Перевод организации",
            "operationAmount": {"amount": 500.0, "currency": {"name": "руб."}}
        }
    ]


def test_mask_card_number():
    """Проверка маскировки номера карты"""
    input_str = "Maestro 1596837868705199"
    expected_output = "Maestro 1596 83** **** 5199"
    assert mask_nuber(input_str) == expected_output


def test_mask_account_number():
    """Проверка маскировки номера счета"""
    input_str = "Счет 64686473678894779589"
    expected_output = "Счет **9589"
    assert mask_nuber(input_str) == expected_output


def test_no_mask_needed():
    """Проверка, что другие данные не маскируются"""
    input_str = "Проверочные данные"
    expected_output = input_str
    assert mask_nuber(input_str) == expected_output


def test_date_formatting(data):
    """Проверка форматирования даты"""
    output = data_format(data)
    assert output[0]["date"] == "03.07.2019"
    assert output[1]["date"] == "23.03.2018"


def test_masking(data):
    """Тест маскировки тестовых данных"""
    output = data_format(data)
    assert output[0]["from"] == "Maestro 1596 83** **** 5199"
    assert output[0]["to"] == "Счет **9589"
    assert output[1]["from"] == "Счет **7890"
    assert output[1]["to"] == "Счет **4188"
