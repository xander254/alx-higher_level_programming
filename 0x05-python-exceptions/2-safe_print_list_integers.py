#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        for y in range(x):
            if isinstance(my_list[y], int):
                print("{}".format(my_list[y]), end="")
                counter += 1
        print()
    except IndexError as error:
        return error
    return counter
