#!/usr/bin/python3

for number in range(1,100):
    if number == 99:
        print("{:d}".format(number))
    else:
        print("{:02}".format(number),end=", ")
    