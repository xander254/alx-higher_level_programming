#!/usr/bin/python3
for digit1 in range(0,9):
    for digit2 in range((digit1 + 1), 10):
        if (digit1 == 0 and digit2 == 9):
            print(f"{digit1}{digit2}", end="")
        else:
            print(f"{digit1}{digit2}", end=", ")
print()
