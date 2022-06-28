#!/usr/bin/python3
for r in range(97, 123):
    if chr(r) == 'e':
        continue
    if chr(r) == 'q':
        continue
    print("{}".format(chr(r)), end='')
