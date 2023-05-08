import func
import os

# файл с данными
file_path = os.path.join("../tmp/operations.json")


def main():
    # загрузка данных из файла
    data = func.load_data(file_path)
    # фильтрация данных
    data_filtered = func.filters_operations(data)
    # сортировка данных
    data_sort = func.sort_date(data_filtered)
    # форматирование данных
    data_format = func.data_format(data_sort)
    # выдача последних операций
    data_work = func.adding_last_operations(data_format)
    # вывод операций
    for data in data_work:
        print(f""
              f"{data['date']} {data['description']}\n"
              f"{data['from']} -> {data['to']}\n"
              f"{data['amount']} {data['currency']}\n")


if __name__ == "__main__":
    main()
