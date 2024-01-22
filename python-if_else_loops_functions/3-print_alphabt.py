#!/usr/bin/python3

for code in range(ord('a'), ord('z') + 1):
    if code == 113 or code == 101:
        continue
    print("{}".format(chr(code)), end="")
