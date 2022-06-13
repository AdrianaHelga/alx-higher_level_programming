#!/usr/bin/python3
for a in range(0, 9):
    for b in range(1, 10):
        if a < b and a != b and a < 8:
            print("{}{}".format(a, b), end=", ")
        elif a < b and a != b and a == 8:
            print("{}{}".format(a, b))
