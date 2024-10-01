#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for y in range(x):
        try:
            if isinstance(my_list[y], int):
                print("{}".format(my_list[y]), end="")
                counter += 1
        except IndexError:
            break
    print()
    return counter
