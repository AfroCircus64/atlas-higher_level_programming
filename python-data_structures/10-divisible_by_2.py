#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiple = []
    for element in my_list:
        multiple.append(True if not element % 2 else False)
    return multiple
