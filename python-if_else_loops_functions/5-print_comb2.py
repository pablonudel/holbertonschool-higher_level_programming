#!/usr/bin/python3

for i in range(0, 100):
    if i == 99:
        i = "{:02d}".format(i)
        end = None
    else:
        i = "{:02d}".format(i)
        end = ", "
    print(i, end=end)
