import json
import os
from random import randint


def gen_random_array(size, min_, max_):
    arr = list()
    for i in range(0, size):
        arr.append(randint(min_, max_))
    return arr


def gen_data():
    with open("data.txt", "w", encoding="utf-8") as f:
        json.dump(gen_random_array(1000, 0, 5000), f)


def read_arr():
    if not os.path.exists("data.txt"):
        gen_data()
    with open("data.txt", "r") as f:
        return json.load(f)


if __name__ == "__main__":
    print(type(read_arr()))
