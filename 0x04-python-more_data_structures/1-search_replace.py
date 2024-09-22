#!/usr/bin/python3
# Define Func Name
def search_replace(my_list, search, replace):
    new_list = list(my_list)
    # Iterate thru' all elements in list
    for i in range(len(new_list)):
        # Check if it is equal to search
        if new_list[i] == search:
            # if so replace it with replace else return list
            new_list[i] = replace
    return new_list
