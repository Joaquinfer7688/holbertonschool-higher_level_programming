#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        print(f"0{i}", end=', ')
    else:
        print("{}".format(i), end=', ' if i != 99 else '\n')
