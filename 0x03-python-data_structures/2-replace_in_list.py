#!/usr/bin/python3
# Func definition
def replace_in_list(my_list, idx, element):
    # Check if idx is negative, if so return the original list
    if idx < 0:
        return my_list
    # Check if idx is out of range, if so return original list
    if idx >= len(my_list):
        return my_list
    # Replace item at index
    my_list[idx] = element
    return my_list
