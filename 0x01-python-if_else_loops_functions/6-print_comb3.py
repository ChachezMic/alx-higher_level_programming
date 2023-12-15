#!/usr/bin/python3
for k in range(0, 9):
    for r in range(k+1, 10):
        if k < 8:
            print("{}{}".format(k % 10, r % 10), end=", ")
        else:
            print("{}{}".format(k % 10, r % 10), end="\n")
