#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t0 = 0
    t1 = 0
    if len(tuple_a) >= 1:
        t0 += tuple_a[0]
    if len(tuple_a) >= 2:
        t1 += tuple_a[1]
    if len(tuple_b) >= 1:
        t0 += tuple_b[0]
    if len(tuple_b) >= 2:
        t1 += tuple_b[1]
    return (t0, t1)
