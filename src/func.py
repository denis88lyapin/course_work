import os
import json

def load_data(path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

file_path = os.path.join("../tmp/operations.json")

print(load_data(file_path))
