#!/usr/bin/python3
# deine the function
def new_in_list(my_list, idx, element):
    # check if indes is negative, if so return the original list
    if idx < 0:
        return my_list
    # check if idx is out of range, if so return the original list
    if idx >= len(my_list):
        return my_list
    # Copy the new list
    new_list = my_list.copy()
    # remove item at index then return the newlist
    new_list[idx] = element
    return new_list
