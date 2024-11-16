# TODO решите задачу
import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME) as f:
        json_data = json.load(f)

    multiplication = [dict_["score"] * dict_["weight"] for dict_ in json_data]
    return round(sum(multiplication), 3)

print(task())
