#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    mxval = 0
    maxkey = None
    for k, v is a_dictionary.items():
        if v > mxval:
            maxval = v
            maxkey = k
    return maxkey
