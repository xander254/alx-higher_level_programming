#!/usr/bin/python3
# define the function
def add_tuple(tuple_a=(), tuple_b=()):
    # access the elements of a tuple using a loop,add them,store
    # them in another tupple.
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
    elif len(tuple_b) < 2:
        tuple_b = tuple_b + (0,) * (2 - len(tuple_b))
    first_sum = tuple_a[0] + tuple_b[0]
    second_sum = tuple_a[1] + tuple_b[1]
    new_tuple = (first_sum, second_sum)
    return new_tuple
