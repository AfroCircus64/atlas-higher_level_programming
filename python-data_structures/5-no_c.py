#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            string += c
    return string
