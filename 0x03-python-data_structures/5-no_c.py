#!/usr/bin/python3
# define the function
def no_c(my_string):
    # find the characters and remove them in a loop
    new_string = my_string.translate({ord(i): None for i in 'cC'})
    my_string = new_string
    return my_string
