#!/usr/bin/python3
i = 0
for alpha in reversed(range(ord('a'), ord('z')+1)):
    if i % 2 == 1:
        print(chr(alpha).upper(), end='')
    else:
        print(chr(alpha), end='')
    i += 1
