from ExternalNaturalMergeSort import *
from tools import *
import timeit

file_name = file_choose()
print(file_name)


def count(loops):
    start = timeit.default_timer()
    timers_list = []
    for loop in range(loops):
        file_copy = "F.txt"
        copy_to_another_and_split(file_name, file_copy)
        test = 100
        external_natural_merge_sort(file_copy, timers_list)
    print("")
    print("Estimate time for 100 runs timeit_counter: ", (timeit.default_timer() - start)/loops)

    sum = 0
    for i in range(len(timers_list)):
        sum += timers_list[i]
    print("Estimate time for 100 runs (list_counter): ", (sum/loops))

count(100)

