#!/usr/bin/python3
"""
a function that divides 2 integers
and prints the result.
"""


def safe_print_division(a, b):
    result = (lambda a, b: a / b)
    try:
        result = a / b
        return (result)
    except(ZeroDivisionError):
        result = None
        return None
    finally:
        print("Inside result: {}".format(a))
