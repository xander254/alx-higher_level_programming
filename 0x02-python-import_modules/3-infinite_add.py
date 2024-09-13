#!/usr/bin/python3
import sys
if __name__ == "__main__":
    def add_args():
        total_sum = 0
        argv = sys.argv
        length = len(argv)
        if length == 1:
            print("0")
            return
        for args in range(1, length):
            total_sum += int(argv[args])
        print("{}".format(total_sum))

add_args()
