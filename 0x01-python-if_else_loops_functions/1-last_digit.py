#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    n = (-1 * number) % 10
    n *= -1
else:
    n = number % 10
print(f"Last digit of {number:d} is {n:d}", end=' ')
if n > 5:
    print(f"and is greater than 5")
elif n == 0:
    print(f"and is 0")
elif n < 6:
    print(f"and is less than 6 and not 0")
