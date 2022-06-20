#!/usr/bin/python3
"""
a function that prints an integer with "{:d}".format()
"""


def safe_print_integer(value):
    try:
        int_val = int(value)
        print("{:d}".format(int_val))
        return True
    except (ValueError, TypeError):
        return False
