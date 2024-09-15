#!/usr/bin/python3
# Define function
def print_reversed_list_integer(my_list=[]):
    # Use a loop to access all integers in reverse
    for element in reversed(my_list):
        # Print intergers using an index
        print("{}".format(element))
