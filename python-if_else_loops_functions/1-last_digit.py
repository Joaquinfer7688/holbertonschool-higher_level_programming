#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if number < 0:
    last_digit = last_digit - 10
print(f"Last digit of {number} is {last_digit} and is", end=' ')
if last_digit == 0:
    print(f"0")
elif last_digit > 5:
    print(f"greater than 5")
else:
    print(f"less than 6 and not 0")
