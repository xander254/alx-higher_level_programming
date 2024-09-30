#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for y in range(0, x):
            if isinstance(my_list[y], int):
                print("{:d}".format(y), end="")
                counter += 1
        print()
    except IndexError:
            print("Error")
    return counter
