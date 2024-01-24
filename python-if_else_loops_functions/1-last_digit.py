#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last digit = number % 10
if last digit == 0:
    print("is 0")
if number < 0:
    last digit = last digit -10
elif last digit > 5:
    print("is greater than 5")
else:
    print("less than 6 and not 0")
