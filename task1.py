# TODO решите задачу
import json

def task() -> float:

    filename = "input.json"
    with open(filename) as file:
        data = json.load(file)
    sum_proizv = 0
    for elem in data:
        sum_proizv += elem['score'] * elem['weight']

    return round(sum_proizv, 3)


print(task())
