#!/usr/bin/python3
# define our function
def print_matrix_integer(matrix=[[]]):
    # initiate twoo loops to loop over the row and element then print
    for row in matrix:
        for num in row:
            if num >= len(matrix):
                print("{}".format(num), end=" ")
            else:
                print("{}".format(num), end=" ")
        print()
