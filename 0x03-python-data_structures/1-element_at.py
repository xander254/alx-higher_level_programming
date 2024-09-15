#!/usr/bin/python3
def element_at(my_list, idx):
    # check if index is negative
    if idx < 0:
        return None
    # Check if index is out of range
    if idx > len(my_list):
        return None
    # Access items
    return my_list[idx]
