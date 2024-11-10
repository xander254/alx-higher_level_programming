#!/usr/bin/python3
# a function that finds all multiples of 2 in a list

def divisible_by_2(my_list=[]):
    """
     a function that finds all multiples of 2 in a list
     """
    new_list = []
    i = 0
    while i < len(my_list):
        if (my_list[i] % 2) == 0:
            new_list.append("True")
        else:
            new_list.append("False")
        i += 1
    return new_list
