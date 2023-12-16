#!/usr/bin/python3
def uppercase(str):

    str_update = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            str_update += chr(ord(c) - 32
        else:
        str_update += c
            print("{}".format(str_update), end="\n")

