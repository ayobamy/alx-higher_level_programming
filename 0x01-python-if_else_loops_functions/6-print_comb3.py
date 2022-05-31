#!/usr/bin/python3
for j in range(10):
    for k in range(j + 1, 10):
        if (j == 8 and k == 9):
            print("{0:d}{1:d}".format(j, k))
            continue
        print("{0:d}{1:d}".format(j, k), end=', ')
