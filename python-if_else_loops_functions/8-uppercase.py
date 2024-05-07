#!/usr/bin/python3
def uppercase(str):
    for c in str:
        k = ord(c)
        if 97 <= k <= 122:
            k -= 32
        print("{}".format(chr(k)), end="")
    print()
