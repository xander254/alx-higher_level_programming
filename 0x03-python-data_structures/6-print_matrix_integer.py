#!/usr/bin/python3
# define our function
def print_matrix_integer(matrix=[[]]):
    # initiate twoo loops to loop over the row and element then print
    for row in matrix:
        for num in row:
            the_matrix = "{}".format(num)
            if num >= len(matrix):
                print(the_matrix, end="")
            else:
                print(the_matrix, end=" ")
        print()
