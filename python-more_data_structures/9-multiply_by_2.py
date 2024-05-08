#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary = a_dictionary.copy()
    for key, value in dictionary.items():
        dictionary[key] = value * 2
    return dictionary
