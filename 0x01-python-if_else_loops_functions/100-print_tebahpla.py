#!/usr/bin/python3
for alpha in reversed(range(ord('a'), ord('z')+1)):
    if alpha % 2 == 1:
        alpha = ord(chr(alpha).upper())
    print(chr(alpha), end='')
