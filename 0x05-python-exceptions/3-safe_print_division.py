#!/usr/bin/python3
"""
a function that divides 2 integers
and prints the result.
"""


def safe_print_division(a, b):
    def div(n, m):
        return (n / m)
    try:
        res = div(a, b)
        return a
    except ZeroDivisionError:
        res = None
        return None
    finally:
        print("Inside result: {}".format(res))