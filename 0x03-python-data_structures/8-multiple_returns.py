#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence:
        if len(sentence) != 0:
            return (len(sentence), sentence[0])
        else:
            return (sentence[0], None)
