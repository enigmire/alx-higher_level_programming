#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for loop in range(4, 6):
            c = add(c, loop)
        return c
    else:
        return (sub(a, b))
