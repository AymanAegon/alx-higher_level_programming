#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


if __name__ == "__main__":
    nbr = len(argv)
    res = 0
    print(argv)
    if nbr != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    opp = argv[2]
    b = int(argv[3])
    if opp == '+':
        res = add(a, b)
    elif opp == '*':
        res = mul(a, b)
    elif opp == '/':
        res = div(a, b)
    elif opp == '-':
        res = sub(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, opp, b, res))
