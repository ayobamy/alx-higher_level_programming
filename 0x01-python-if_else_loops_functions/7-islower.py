#!/usr/bin/python3
def islower(c):
    """a function that check for lowercase
    characters and returns true or false otherwise"""
    if (ord(c) >= 97 and ord(c) <= 122):
        return True
    else:
        return False
