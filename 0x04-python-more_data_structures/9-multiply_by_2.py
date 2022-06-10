#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    a function that returns a new dictionary
    with all values multiplied by 2
    """
    a_dictionary.update((k, v * 2) for k, v in a_dictionary.items())

    return a_dictionary
