import time

from app.mergesort.merge_sort_with_function_annotation import \
    merge_sort as merge_sort_with_function_annotation
from app.mergesort.gen_data import read_arr
from app.mergesort.merge_sort import merge_sort

arr = read_arr()


def timing_merge_sort():
    total = 0
    for i in range(0, 5):
        start_time = time.time() * 1000
        merge_sort(arr, 0, len(arr) - 1)
        stop_time = time.time() * 1000
        print("#{} {} ms".format(i + 1, stop_time - start_time))
        total += stop_time - start_time
    print("Average {} ms".format(total / 5))


def timing_merge_sort_with_function_annotation():
    total = 0
    for i in range(0, 5):
        start_time = time.time() * 1000
        merge_sort_with_function_annotation(arr, 0, len(arr) - 1)
        stop_time = time.time() * 1000
        print("#{} {} ms".format(i + 1, stop_time - start_time))
        total += stop_time - start_time
    print("Average {} ms".format(total / 5)) 

