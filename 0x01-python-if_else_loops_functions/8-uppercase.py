#!/usr/bin/python3
def uppercase(str):
    for m in str:
        if (ord(m) >= 97 and ord(m) <= 122):
            m = chr(ord(m) - 32)
        print("{}".format(m), end='')
    print()
