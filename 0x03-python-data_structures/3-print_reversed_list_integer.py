#!/usr/bin/python3
# Define function
def print_reversed_list_integer(my_list=[]):
    # Use a loop to access all integers in reverse
    if my_list is None:
        return None
    for element in my_list[::-1]:
        # Print intergers using an index
        print("{:d}".format(element))
