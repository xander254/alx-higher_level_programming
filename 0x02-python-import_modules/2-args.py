#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    n = len(argv)
    if n == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(n - 1))
    for args in range(1, n):     
        print("{}: {}".format(args, argv[args]))
