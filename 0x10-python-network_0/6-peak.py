#!/usr/bin/python3
""" A module to find the peak integer"""
def find_peak(list_of_integers):
    """ A function that finds the peak integer in a list of ints"""
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    start = 0
    end = len(list_of_integers) - 1

    while start <= end:
        mid = (start + end) // 2

        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
             (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
             return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            end = mid -1
        else:
            start = mid + 1
