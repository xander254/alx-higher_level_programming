#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    hidden_vars = dir(hidden_4)
    length = len(hidden_vars)
    for num in hidden_vars:
        if not num.startswith("_"):
            print("{}".format(num))
