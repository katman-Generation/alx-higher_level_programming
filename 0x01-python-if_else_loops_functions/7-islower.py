#!/usr/bin/python3
def islower(c):
    sl = []
    for i in range(97, 123):
        sl.append("{:c}".format(i))
    if c in sl:
        print(True)
    else:
        print(False)
