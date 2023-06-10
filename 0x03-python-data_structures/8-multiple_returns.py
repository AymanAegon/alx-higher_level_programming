#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = ''
    if length >= 1:
        first = sentence[0]
    return (length, first)
