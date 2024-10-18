#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedDict = dict(sorted(a_dictionary.items()))
    for key, value in sortedDict.items():
        print("{}: {}".format(key, value), end="\n")
