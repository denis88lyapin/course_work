import func
import os


file_path = os.path.join("../tmp/operations.json")
def main():

    data = func.load_data(file_path)

    data_filtered = func.filters_operations(data)

    data_sort = func.sort_date(data_filtered)

    data_format = func.data_format(data_sort)

    data_work = func.adding_last_operations(data_format)

    for data in data_work:
        print(f""
              f"{data['date']} {data['description']}\n"
              f"{data['from']} -> {data['to']}\n"
              f"{data['amount']} {data['currency']}\n")


if __name__ == "__main__":
    main()







