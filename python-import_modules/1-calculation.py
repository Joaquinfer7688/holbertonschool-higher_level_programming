#!/usr/bin/python3
if __name__ == "__main__"
from calculator_1 import sub, div, add, mul
a = 10
b = 5
c = add(a, b)
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
