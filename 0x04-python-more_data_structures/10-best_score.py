#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:

        sorted_keys = sorted(a_dictionary)
        highest_score = sorted_keys[-1]
        return highest_score
    return None
