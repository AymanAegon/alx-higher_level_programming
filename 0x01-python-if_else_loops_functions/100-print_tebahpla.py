#!/usr/bin/python3
for alpha in reversed(range(ord('a'), ord('z')+1)):
    if alpha % 2 == 1:
        print(chr(alpha).upper(), end='')
    else:
        print(chr(alpha), end='')
