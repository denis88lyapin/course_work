import os
import json

def load_data(path):
    """
    Загружает данные из файла с операциями
    """
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def filters_operations(data):
    """
    Возвращает отфильтрованные операции
    :param data: список всех операций
    :return: список успешных опрераций
    """
    cleared_operations = []
    for operation in data:
        if operation.get("state") == "EXECUTED":
            cleared_operations.append(operation)
    return cleared_operations


file_path = os.path.join("../tmp/operations.json")
a = load_data(file_path)

print(filters_operations(a))
