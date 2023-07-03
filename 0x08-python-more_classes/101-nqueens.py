#!/usr/bin/python3
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)
if N < 4:
    print("N must be at least 4")
    exit(1)

arr = []
for k in range(N - 2):
    j = k + 1
    for i in range(N):
        arr.append([i, j])
        if j == N-1:
            j = 0
        else:
            j = (j+2)%N
    print(arr)
    arr = []
