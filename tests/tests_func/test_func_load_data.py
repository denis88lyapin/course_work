from src.func import load_data
import json
import pytest


@pytest.fixture
def json_data(tmp_path):
    """Временный файл с данными"""
    data = {'operations': [{'type': 'deposit', 'amount': 100}, {'type': 'withdraw', 'amount': 50}]}
    json_file = tmp_path / 'data.json'
    with open(json_file, 'w') as f:
        json.dump(data, f)
    return json_file


def test_load_data_with_valid_data(json_data):
    """Проверка, что данные успешно загружены"""
    data = load_data(json_data)
    assert data == {'operations': [{'type': 'deposit', 'amount': 100}, {'type': 'withdraw', 'amount': 50}]}

def test_load_data_with_invalid_file_path():
    """"Проверка ошибки загрузки данных"""
    with pytest.raises(FileNotFoundError):
        load_data("не указал файл")

def test_load_data_with_invalid_json_data(tmp_path):
    """Проверка ошибки неверного формата данных"""
    invalid_json_file = tmp_path / 'invalid_data.json'
    with open(invalid_json_file, 'w') as f:
        f.write('not json data')
    with pytest.raises(ValueError):
        load_data(invalid_json_file)
