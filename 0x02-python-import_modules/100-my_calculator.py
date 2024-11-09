#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    args = sys.argv
    length = len(args)
    if length != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if (
        sys.argv[2] != '+' and
        sys.argv[2] != '-' and
        sys.argv[2] != '*' and
        sys.argv[2] != '/'
    ):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if (sys.argv[2] == '+'):
        print("{} + {} = {}".format(a, b, add(a, b)))
    if (sys.argv[2] == '/'):
        print("{} / {} = {}".format(a, b, div(a, b)))
    if (sys.argv[2] == '*'):
        print("{} * {} = {}".format(a, b, mul(a, b)))
    if (sys.argv[2] == '-'):
        print("{} - {} = {}".format(a, b, sub(a, b)))
