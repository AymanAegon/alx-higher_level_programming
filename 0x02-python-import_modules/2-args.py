#!/usr/bin/python3
import sys


l = len(sys.argv)
if __name__ == "__main__":
    if l > 1:
        print("{} arguments:".format(l - 1))
        for i in range(1, l):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("0 arguments.")
