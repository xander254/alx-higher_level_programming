#!/usr/bin/python3
# def func
def only_diff_elements(set_1, set_2):
    diff = (set_1.difference(set_2))
    diff2 = (set_2.difference(set_2))
    diffval1 = list(diff)
    diffval2 = list(diff2)
    result = diffval1 + diffval2
    return result
