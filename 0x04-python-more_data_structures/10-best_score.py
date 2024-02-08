#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:

        sorted_keys = sorted(a_dictionary, key=a_dictionary.get)
        highest_score_key = sorted_keys[-1]
        return highest_score_key
    return None
