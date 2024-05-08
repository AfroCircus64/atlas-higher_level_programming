#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list = []
    for element in my_list:
        if element != search:
            list.append(element)
        else:
            list.append(replace)
    return list
