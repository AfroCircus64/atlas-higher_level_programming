#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        difference = a / b
    except (ZeroDivisionError):
        difference = None
    finally:
        print("Inside result: {}".format(difference))
    return difference
