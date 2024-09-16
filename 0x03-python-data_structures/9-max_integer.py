#!/usr/bin/python3
# define function
def max_integer(my_list=[]):
    length = len(my_list)
    # check if list is empty, is so return None
    if len(my_list) == 0:
        return None
    else:
        i = len(my_list) - 1
        while i > 0:
            j = 0
            while j < i:
                if my_list[j] > (my_list[j + 1]):
                    temp = my_list[j]
                    my_list[j] = (my_list[j + 1])
                    (my_list[j + 1]) = temp
                j += 1
            i -= 1
        return my_list[length - 1]
