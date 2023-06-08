#!/usr/bin/python3
import sys


if __name__ == "__main__":
    nbr = len(sys.argv)
    if nbr== 2:
        print("{} argument:".format(nbr - 1))
        print("{}: {}".format(1, sys.argv[1]))
    elif nbr > 2:
        print("{} arguments:".format(nbr - 1))
        for i in range(1, nbr):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("0 arguments.")
