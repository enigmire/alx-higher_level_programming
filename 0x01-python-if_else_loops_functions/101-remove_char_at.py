#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        ch = str[:n] + str[n + 1:]
        return (ch)
    else:
        return (str)
