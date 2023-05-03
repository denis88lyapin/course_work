import os
import json
from datetime import datetime


def load_data(path):
    """
    Загружает данные из файла с операциями
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Файл {path} не найден")
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        raise ValueError((f"Файл {path} содержит неверный формат данных"))
    return data


def filters_operations(data):
    """
    Возвращает отфильтрованные операции, убирает операции без необходимых для вывода данных
    :param data: список всех операций
    :return: список отфильтрованных опрераций, отсортированный по дате и времени
    """
    cleared_operations = []
    for operation in data:
        if all(key in operation and operation[key] for key in ["state", "date", "description", "from", "to", "operationAmount"]):
            if operation.get("state") == "EXECUTED":
                cleared_operations.append(operation)
    cleared_operations.sort(key=lambda x: datetime.strptime(x.get("date"), "%Y-%m-%dT%H:%M:%S.%f"))
    return cleared_operations


def adding_last_operations(data):
    """
    Возвращает список последних операций
    :param data: список операций
    :return: списмок последних операций
    """
    if len(data) == 0:
        return f"У Вас нет проведенных операций"
    elif len(data) < 5:
        return data
    else:
        return data[-5:]


# file_path = os.path.join("../tmp/operations.json")
# a = load_data(file_path)
#
# print(adding_last_operations(filters_operations(a)))