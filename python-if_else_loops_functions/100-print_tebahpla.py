#!/usr/bin/python3

for i in range(ord('z'), ord('a') - 1, -1):

    i = i - ord('z') + ord('Z') if i % 2 != 0 else i
    print(chr(i), end='')
