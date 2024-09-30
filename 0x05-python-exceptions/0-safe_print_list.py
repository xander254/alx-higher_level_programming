#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for y in range(1, x+1):
        try:
            print("{}".format(y), end="")
            counter += 1
        except:
            print("Error")
    print()	
    return counter
