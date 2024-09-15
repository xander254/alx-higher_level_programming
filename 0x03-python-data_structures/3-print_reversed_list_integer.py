#!/usr/bin/python3
# Define function
def print_reversed_list_integer(my_list=[]):
    # Reverse the list
    my_list.reverse()
    # Use a loop to access all integers
    for index in range(len(my_list)):
        # Print intergers using an index
        print("{}".format((my_list[index])))
