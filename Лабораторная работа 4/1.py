# TODO решите задачу
import json
def task() -> float:
    summ = 0
    with open("input.json", "r") as read_file:
        data = json.load(read_file)


    for i in range(len(data)):
        summ += data[i]["score"]*data[i]["weight"]

    summ = round(summ, 3)

    return summ


print(task())