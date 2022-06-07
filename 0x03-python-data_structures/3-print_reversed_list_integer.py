#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range (len(my_list)):
        if i > 0:
            print(my_list[-i])
    print(my_list[0])
