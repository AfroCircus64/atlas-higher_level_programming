#!/usr/bin/python3
"""Defines a script that adds all args to a python list then save"""


from sys import argv
load_from = __import__('6-load_from_json_file').load_from_json_file
save_to = __import__('5-save_to_json_file').save_to_json_file

try:
    list_obj = load_from("add_item.json")
except:
    list_obj = []

list_obj += argv[1:]
save_to(list_obj, "add_item.json")
