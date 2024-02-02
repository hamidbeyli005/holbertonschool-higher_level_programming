#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ''
    for i in text:
        line += i
        if i == ':' or i == '?' or i == '.':
            print(line.strip())
            print()
            line = ''

    if line:
        print(line.strip())
