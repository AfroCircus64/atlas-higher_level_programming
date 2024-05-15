#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    i = 0
    for element in my_list:
        if element > i:
            i = element
    return i
