#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    len1 = len(tuple_a)
    len2 = len(tuple_b)

    a1 = tuple_a[0] if len1 > 0 else 0
    a2 = tuple_a[1] if len1 > 1 else 0
    b1 = tuple_b[0] if len2 > 0 else 0
    b2 = tuple_b[1] if len2 > 1 else 0

    return ("{}".format((a1 + b1, a2 + b2)))
