#!/usr/bin/python3
# Define the function
def print_list_integer(my_list=[]):
    # loop through the list using the length of the list
    for index in range(len(my_list)):
        # print items at a specific index
        print("{}".format(my_list[index]))
