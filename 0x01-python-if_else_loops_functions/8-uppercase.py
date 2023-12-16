#!/usr/bin/python3
def uppercase(str):

    str_update = ""

    for i in str:

        if ord(i) >= 97 and ord(i) <= 122:
            str_update += chr(ord(i) - 32)
        else:
            str_update += i

    print("{}".format(str_update), end="\n")
