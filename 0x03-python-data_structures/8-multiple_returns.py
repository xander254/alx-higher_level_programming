#!/usr/bin.python3
# Func defination
def multiple_returns(sentence):
    # Check if sentence is empty, if so return None
    # return as expected
    if sentence == "":
        return None
    length = len(sentence)
    first = sentence[0]
    return length, first
