#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    nbr = len(argv)
    sum = 0
    for i in range(1, nbr):
        sum += int(argv[i])
    print(sum)
