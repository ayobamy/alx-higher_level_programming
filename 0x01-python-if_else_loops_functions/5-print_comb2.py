#!/usr/bin/python3
for comb in range(0, 100):
    if comb == 99:
        print("{0:d}".format(comb))
        continue
    print("{0:02}".format(comb), end=', ')
