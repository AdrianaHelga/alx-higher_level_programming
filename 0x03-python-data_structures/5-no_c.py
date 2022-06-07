#!/usr/bin/env python3
def no_c(my_string):
    new_string = my_string[:]

    for i in range (len(new_string)):
        if new_string[i] == 'c' or new_string[i] == 'C':
            new_string[i] == []
            return new_string
