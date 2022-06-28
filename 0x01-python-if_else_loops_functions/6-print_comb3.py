#!/usr/bin/python3
for r in range(9):
    for i in range(r+1, 10):
        if r == 8 and i == 9:
            print(f"{r}{i}".format(r, i))
        else:
            print(f"{r}{i},".format(r, i), end=" ")
