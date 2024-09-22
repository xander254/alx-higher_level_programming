#!/usr/bin/python3
# Func defination
def uniq_add(my_list=[]):
    # convert list to set (find unique)
    unique_set = set(my_list)
    # sum them up
    result = sum(unique_set)
    return result
