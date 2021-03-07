from tools import *
import os
import timeit


def merging(f_name, f1_name, f2_name, timers_list):
    """splitting"""
    start = timeit.default_timer()
    counter_splits = 0
    counter_merges = 0
    counter_more_or_less_split = 0
    while True:
        with open(f_name, "r") as f, open(f1_name, "w") as f1, open(f2_name, "w") as f2:
            active_file = 'f1'
            num = read_int(f)
            write_to_active_file(active_file, num, f1, f2)
            temp = num
            while num is not None:
                num = read_int(f)
                if num is None:
                    break
                counter_more_or_less_split += 1
                if num >= temp:
                    write_to_active_file(active_file, num, f1, f2)
                else:
                    active_file = swap_active_files(active_file)
                    write_to_active_file(active_file, num, f1, f2)
                temp = num

        if os.stat(f2_name).st_size == 0:
            break
        counter_splits += 1
        f1.close()
        f2.close()
        f.close()

        """merging"""
        with open(f_name, "w") as f, open(f1_name, "r") as f1, open(f2_name, "r") as f2:
            num_f1 = read_int(f1)
            num_f2 = read_int(f2)

            while num_f1 is not None and num_f2 is not None:
                run_f1 = False
                run_f2 = False
                while run_f1 is False and run_f2 is False:
                    if num_f1 <= num_f2:
                        write_to_main_file(f, num_f1)
                        num_f1 = read_int(f1)
                        run_f1 = end_of_range(num_f1)

                    else:
                        write_to_main_file(f, num_f2)
                        num_f2 = read_int(f2)
                        run_f2 = end_of_range(num_f2)
                    counter_more_or_less_split += 1
                while run_f1 is False:
                    write_to_main_file(f, num_f1)
                    num_f1 = read_int(f1)
                    run_f1 = end_of_range(num_f1)

                while run_f2 is False:
                    write_to_main_file(f, num_f2)
                    num_f2 = read_int(f2)
                    run_f2 = end_of_range(num_f2)

            run_f1 = False
            run_f2 = False
            while num_f1 is not None and run_f1 is False:
                write_to_main_file(f, num_f1)
                num_f1 = read_int(f1)

            while num_f2 is not None and run_f2 is False:
                write_to_main_file(f, num_f2)
                num_f2 = read_int(f2)

        counter_merges += 1
        f.close()
        f1.close()
        f2.close()

    end = timeit.default_timer()
    print("counter_splits: ", counter_splits)
    print("counter_merge: ", counter_merges)
    print("counter_more_or_less: ", counter_more_or_less_split)
    print("Working time: ", end - start, "s")
    timers_list.append(end - start)


def external_natural_merge_sort(f_name, timers_list):
    f1_name = "f1.txt"
    f2_name = "f2.txt"
    f1 = open(f1_name, "w")
    f2 = open(f2_name, "w")
    f1.close()
    f2.close()
    with open(f_name, "r") as input_file:
        data_from_input_file = list(map(int, input_file.readlines()))
        print(data_from_input_file)
    merging(f_name, f1_name, f2_name, timers_list)
    with open(f_name, "r") as input_file:
        data_from_input_file = list(map(int, input_file.readlines()))
        print(data_from_input_file)


