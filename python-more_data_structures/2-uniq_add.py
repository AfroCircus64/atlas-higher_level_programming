#!/usr/bin/python3
def uniq_add(my_list=[]):
    list = set(my_list)
    sum = 0
    for num in list:
        sum += num
    return sum
