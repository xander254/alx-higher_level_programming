#!/usr/bin/python3
# define the function
def delete_at(my_list=[], idx=0):
    # check if index is < 0 or out of range, if return list
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    del my_list[idx]
    new_list = my_list
    return new_list
