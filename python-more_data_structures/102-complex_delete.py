#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_key = []
    for key, val in a_dictionary.items():
        if val == value:
            delete_key.append(key)
    for key in delete_key:
        del a_dictionary[key]
    return a_dictionary
