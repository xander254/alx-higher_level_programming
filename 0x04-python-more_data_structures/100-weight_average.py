#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    total_sum = 0
    weight = 0

    for value, weight in my_list:
        total_sum += (value * weight)
        weight += weight

    return total_sum / weight if weight != 0 else 0
