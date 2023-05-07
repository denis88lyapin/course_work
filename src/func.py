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
        raise ValueError(f"Файл {path} содержит неверный формат данных")
    return data


def filters_operations(data):
    """
    Возвращает отфильтрованные операции, убирает операции без необходимых для вывода данных
    :param data: список всех операций
    :return: список отфильтрованных опрераций
    """
    cleared_operations = []
    for operation in data:
        if all(key in operation and operation[key] for key in ["state", "date", "description", "from", "to", "operationAmount"]):
            if operation.get("state") == "EXECUTED":
                cleared_operations.append(operation)
    return cleared_operations


def sort_date(data):
    """
    Возвращает отсортированные по дате опенрации
    :param data: список операций
    :return: отсортированнный список операций
    """
    data.sort(key=lambda x: datetime.strptime(x.get("date"), "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    return data


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
        return data[:5]


def data_format(data):
    """
    возвращает список операций в нужном формате
    :param data: список операций
    :return: список операций в нужном формате
    """
    new_format_date = []
    for operation in data:
        date = format_date(operation["date"])
        from_ = mask_nuber(operation["from"])

        # Маскируем данные, аналогично "from"
        to = mask_nuber(operation["to"])
        new_format_date.append({
                                "date": date,
                                "description": operation["description"],
                                "from": from_,
                                "to": to,
                                "amount": operation['operationAmount']['amount'],
                                "currency": operation['operationAmount']['currency']['name']
                                })
    return new_format_date


def mask_nuber(str):
    """
    Маскирует номара карт в формате XXXX XX** **** XXXX
    и счетов в формате **XXXX
    :param str: строка с указанием номера
    :return: строка с замаскированным номером
    """
    if "Maestro" in str or "MasterCard" in str or "Visa" in str:
        card_number = str.split()[-1]
        masked_card_number = f"{card_number[:4]} {card_number[4:6]}{'*' * 2} **** {card_number[-4:]}"
        new_str = str.replace(card_number, masked_card_number)
        # Маскирует номер счета, последнее слово в строке - это номер счета
    elif 'Счет' in str:
        account_number = str.split()[-1]
        masked_account_number = f"**{account_number[-4:]}"
        new_str = str.replace(account_number, masked_account_number)
    else:
        new_str = str
    return new_str


def format_date(date):
    """
    Преобразует дату из в нужный формат
    :param date: дата в формате "%Y-%m-%dT%H:%M:%S.%f"
    :return: дата в формате "%d.%m.%Y"
    """
    date_new = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
    return date_new
