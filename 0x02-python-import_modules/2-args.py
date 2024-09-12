#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    n = len(argv)
    for args in range(1, n):
        if args == 1:
            print("1 argument:")
            print("{}: {}".format((1), argv[1]))
        elif args > 1:
            print("{} arguments:".format(n - 1))
            print("{}: {}".format((n - 2), argv[n - 2]))
