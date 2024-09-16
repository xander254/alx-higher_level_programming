#!/usr/bin/python3
# define our function
def print_matrix_integer(matrix=[[]]):
    # initiate twoo loops to loop over the row and element then print
    for row in matrix:
        for num in range(len(row)):
            if num == len(row) - 1:
                print("{:d}".format(row[num]), end="")
            else:
                print("{:d}".format(row[num]), end=" ")
        print()
