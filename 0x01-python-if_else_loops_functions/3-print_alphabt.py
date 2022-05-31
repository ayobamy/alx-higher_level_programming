#!/usr/bin/python3
for qe in range(97, 123):
    if (qe == 101 or qe == 113):
        continue
    print("{}".format(chr(qe)), end="")
